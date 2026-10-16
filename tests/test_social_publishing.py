"""Offline checks of account binding, publication recovery and prepared assets."""
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from publish_social import Publisher, ApiError, campaign_day, validate_post
from export_social_campaign import x_weight
from PIL import Image

CONFIG = json.loads((ROOT / 'social/publishing.json').read_text())
POSTS = json.loads((ROOT / 'social/outbox.json').read_text())['posts']
ENV = {key: 'offline-test-value' for key in (
    'X_API_KEY', 'X_API_SECRET', 'X_ACCESS_TOKEN',
    'X_ACCESS_TOKEN_SECRET', 'META_PAGE_ACCESS_TOKEN')}


class FakeTransport:
    def __init__(self, wrong=None, failure=None):
        self.calls = []
        self.wrong = wrong
        self.failure = failure

    def request(self, method, url, headers=None, body=None):
        path = urlsplit(url).path
        self.calls.append((method, path, body))
        if method == 'HEAD':
            return {'status': 200, 'content_type': 'image/jpeg'}
        if path == '/2/users/me':
            return {'data': {'username': 'other' if self.wrong == 'x' else 'stayindanang'}}
        if path.endswith('/me'):
            return {'id': 'other' if self.wrong == 'facebook' else CONFIG['expected_facebook_page_id'], 'category': 'Travel'}
        if method == 'GET' and path.endswith('/' + CONFIG['expected_facebook_page_id']):
            return {'instagram_business_account': {'id': 'ig-account'}}
        if method == 'GET' and path.endswith('/ig-account'):
            return {'username': 'other' if self.wrong == 'instagram' else 'stayindananghoianhue'}
        if path.endswith('/container'):
            return {'status_code': 'FINISHED'}
        if method == 'POST':
            if self.failure and path == '/2/tweets':
                raise self.failure
            if path == '/2/media/upload':
                return {'data': {'id': 'uploaded'}}
            if path == '/2/tweets':
                return {'data': {'id': 'tweet'}}
            if path.endswith('/photos'):
                return {'post_id': 'page-photo'}
            if path.endswith('/media'):
                return {'id': 'container'}
            if path.endswith('/media_publish'):
                return {'id': 'instagram-photo'}
        raise AssertionError((method, path))


class PublishingTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.ledger = Path(self.directory.name) / 'ledger.json'

    def publisher(self, transport=None, env=None):
        return Publisher(CONFIG, self.ledger, transport or FakeTransport(),
                         ENV if env is None else env, sleep=lambda _: None)

    def test_missing_credentials_performs_no_requests(self):
        http = FakeTransport()
        with self.assertRaisesRegex(ValueError, 'Missing GitHub Actions secrets'):
            self.publisher(http, {}).verify_accounts(['x', 'facebook', 'instagram'])
        self.assertEqual(http.calls, [])

    def test_any_wrong_identity_blocks_all_publications(self):
        for platform in ('x', 'facebook', 'instagram'):
            with self.subTest(platform=platform):
                http = FakeTransport(wrong=platform)
                publisher = self.publisher(http)
                with self.assertRaises(ValueError):
                    publisher.verify_accounts(['x', 'facebook', 'instagram'])
                self.assertEqual(publisher.verified, set())
                self.assertFalse(any(call[0] == 'POST' for call in http.calls))

    def test_unverified_destination_cannot_publish(self):
        http = FakeTransport()
        with self.assertRaisesRegex(ValueError, 'Verify the destination'):
            self.publisher(http).publish(POSTS[0])
        self.assertEqual(http.calls, [])

    def test_three_platform_routes_and_idempotent_retry(self):
        http = FakeTransport()
        publisher = self.publisher(http)
        publisher.verify_accounts(['x', 'facebook', 'instagram'])
        for post in POSTS[:3]:
            self.assertEqual(publisher.publish(post)['state'], 'published')
        writes = [call for call in http.calls if call[0] == 'POST']
        self.assertEqual(len(writes), 5)
        for post in POSTS[:3]:
            self.assertEqual(publisher.publish(post)['state'], 'already-published')
        self.assertEqual(writes, [call for call in http.calls if call[0] == 'POST'])
        saved = json.loads(self.ledger.read_text())
        self.assertEqual(len(saved['entries']), 3)
        self.assertNotIn('offline-test-value', self.ledger.read_text())

    def test_unknown_outcome_blocks_retry_even_after_restart(self):
        publisher = self.publisher(FakeTransport(failure=ApiError()))
        publisher.verify_accounts(['x'])
        with self.assertRaises(ApiError):
            publisher.publish(POSTS[0])
        self.assertEqual(publisher.ledger['entries']['day-01:x']['state'], 'uncertain')
        restarted = self.publisher()
        restarted.verify_accounts(['x'])
        with self.assertRaisesRegex(ValueError, 'manual review'):
            restarted.publish(POSTS[0])

    def test_known_rejection_can_retry_without_duplicate_success(self):
        publisher = self.publisher(FakeTransport(failure=ApiError(403)))
        publisher.verify_accounts(['x'])
        with self.assertRaises(ApiError):
            publisher.publish(POSTS[0])
        self.assertEqual(publisher.ledger['entries']['day-01:x']['state'], 'failed')
        retry = self.publisher()
        retry.verify_accounts(['x'])
        self.assertEqual(retry.publish(POSTS[0])['state'], 'published')

    def test_campaign_window_uses_calendar_days(self):
        self.assertEqual(campaign_day('2026-10-20', date(2026, 10, 20)), 1)
        self.assertEqual(campaign_day('2026-10-20', date(2026, 11, 18)), 30)
        self.assertIsNone(campaign_day('2026-10-20', date(2026, 10, 19)))
        self.assertIsNone(campaign_day('2026-10-20', date(2026, 11, 19)))

    def test_all_ninety_assets_and_captions_are_valid(self):
        self.assertEqual(len(POSTS), 90)
        for day in range(1, 31):
            self.assertEqual({p['platform'] for p in POSTS if p['day'] == day}, {'x', 'facebook', 'instagram'})
        for post in POSTS:
            asset = validate_post(post)
            with Image.open(asset) as image:
                image.load()
                self.assertEqual(image.format, 'JPEG')
                self.assertEqual(image.size, (post['width'], post['height']))
                if post['platform'] == 'instagram':
                    self.assertTrue(.8 <= image.width / image.height <= 1.91)
            if post['platform'] == 'x':
                self.assertLessEqual(x_weight(post['text']), 280)
            elif post['platform'] == 'instagram':
                self.assertLessEqual(len(post['text']), 2200)
            article = urlsplit(post['blog_url']).path.removeprefix('/stayindanang/')
            self.assertTrue((ROOT / article / 'index.html').is_file(), article)


if __name__ == '__main__':
    unittest.main()
