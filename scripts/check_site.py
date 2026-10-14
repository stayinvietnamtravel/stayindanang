#!/usr/bin/env python3
"""Check the generated site without a server or third-party packages."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, parse_qs, unquote
import json
import xml.etree.ElementTree as ET
from build_site import BASE, home, blog, article, url
from content import LANGUAGES, SLUGS, ARTICLE_DETAILS
from deal_posts import HOTELS, DATA, EXPORT_ROOT, page_pairs, post_path, image_path, social_post, short_post
from hotel_editorial import editorial
from marketplace import CONFIG as AFFILIATE_CONFIG, FEATURED, service_url
from world_destinations import COUNTRIES, CITY_KEYS, REGION_KEYS
from travel_portal import page_pairs as travel_page_pairs, SOURCES as TRAVEL_SOURCES, safe_articles
import struct
import zipfile
import csv
from html import escape

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.alternates = {}
        self.frames = []
        self.images = []
        self.lang = None
        self.canonical = None
        self.script = None
        self.schemas = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'html':
            self.lang = a.get('lang')
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical = a['href']
        if tag == 'link' and a.get('rel') == 'alternate':
            self.alternates[a['hreflang']] = a['href']
        if tag == 'a' and 'hreflang' in a:
            self.links.append(('language', a['href']))
        if tag in ('a', 'link', 'script', 'img'):
            target = a.get('href') or a.get('src')
            if target:
                self.links.append((tag, target))
        if tag == 'iframe':
            self.frames.append(a)
        if tag == 'img':
            self.images.append(a)
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.script = ''

    def handle_data(self, data):
        if self.script is not None:
            self.script += data

    def handle_endtag(self, tag):
        if tag == 'script' and self.script is not None:
            self.schemas.append(json.loads(self.script))
            self.script = None


def check():
    paths = [p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*.html')]
    pages = {}
    for path in paths:
        page = Page()
        page.feed((ROOT/path).read_text(encoding='utf-8'))
        pages[path] = page
        assert page.lang in LANGUAGES, path
        assert page.canonical == url(path), (path, 'canonical')
        assert len(page.ids) == len(set(page.ids)), (path, 'duplicate id')
        assert set(page.alternates) == set(LANGUAGES) | {'x-default'}, (path, 'alternates')
        assert sum(kind == 'language' for kind, _ in page.links) == len(LANGUAGES), (path, 'language selector')
        if any(schema.get('@type') == 'BlogPosting' for schema in page.schemas):
            assert len(page.images) == 1, (path, 'featured image')
            image = page.images[0]
            assert image.get('alt') and image.get('width') and image.get('height'), (path, 'image accessibility')
            assert image['src'].endswith(('.svg','.png')) and not urlsplit(image['src']).scheme, (path, 'local image')
        for kind, link in page.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc:
                continue
            target = (ROOT/path).parent/unquote(parts.path) if parts.path else ROOT/path
            if target.is_dir():
                target /= 'index.html'
            assert target.is_file(), (path, 'missing local target', link)
            assert target.resolve().is_relative_to(ROOT), (path, 'outside site', link)
            if parts.fragment and target.suffix == '.html':
                dest = Page()
                dest.feed(target.read_text(encoding='utf-8'))
                assert unquote(parts.fragment) in dest.ids, (path, 'missing anchor', link)
        assert 'Bookdeal' not in (ROOT/path).read_text(encoding='utf-8') and 'docs.google.com/spreadsheets' not in (ROOT/path).read_text(encoding='utf-8'), (path,'spreadsheet details must remain hidden')
        assert not page.frames, (path, "Trip.com banners must remain removed")
        assert "www.trip.com/partners/ad/" not in (ROOT/path).read_text(encoding="utf-8"), path
        if path==home(page.lang):
            assert 'weather' in page.ids and 'trip-ideas' in page.ids and 'weather-city' in page.ids, (path,'homepage tools')
            assert all(key in page.ids for key in ('booking','destinations','tours','hotels','flights','affiliate-routes')), (path,'discovery navigation')
            html=(ROOT/path).read_text(encoding='utf-8')
            assert 'class="booking-continent"' in html and 'class="booking-country"' in html, (path,'world destination filters')
            assert all(f'value="{key}" data-country=' in html for key in CITY_KEYS), (path,'world destination options')
            targets=[target for kind,target in page.links if kind=='a']
            assert all(link in targets for link in AFFILIATE_CONFIG['services'].values()), (path,'service affiliate routes')
            assert all(h['url'] in targets for h in HOTELS if h['slug'] in FEATURED), (path,'featured property routes')
    expected_paths = {target for lang in LANGUAGES for target in [home(lang), blog(lang), *(article(lang, i) for i in range(len(SLUGS)))]}
    expected_paths.update(path for path, _ in page_pairs(LANGUAGES))
    expected_paths.update(path for path, _ in travel_page_pairs(LANGUAGES))
    assert set(paths) == expected_paths, 'Unexpected or missing generated pages'
    assert len(TRAVEL_SOURCES['official_sites'])==18 and len(TRAVEL_SOURCES['magazines'])==10
    for source in TRAVEL_SOURCES['official_sites']+TRAVEL_SOURCES['magazines']:
        parsed=urlsplit(source['url'])
        assert parsed.scheme=='https' and parsed.hostname and not parsed.username and not parsed.password
    news=json.loads((ROOT/'data/travel_news.json').read_text())
    assert len(safe_articles(news))==len(news['articles']), 'Unsafe cached news URL or title'
    assert len(HOTELS) == 42 and len({h['url'] for h in HOTELS}) == 42
    for hotel in HOTELS:
        assert hotel['url'] in hotel['blog_content_en'] and hotel['url'] in hotel['social_post_en'] and hotel['url'] in hotel['booking_cta_en']
        assert not hotel['hotel_image_url'] and hotel['image_status']=='Needs verified official image URL'
        raw = (ROOT/image_path(hotel)).read_bytes()
        assert raw[:8] == b'\x89PNG\r\n\x1a\n'
        assert struct.unpack('>II', raw[16:24]) == (1600,900), hotel['name']
        assert hotel['url'] in social_post(hotel) and len(short_post(hotel)) <= 280
        export_dir = EXPORT_ROOT/'bookdeal-posts'
        assert (export_dir/(hotel['slug']+'.en.md')).read_text(encoding='utf-8') == hotel['social_post_en']+'\n'
        assert hotel['blog_content_en'] in (export_dir/(hotel['slug']+'.blog.en.md')).read_text(encoding='utf-8')
        for lang in LANGUAGES:
            path = post_path(lang,hotel)
            page = pages[path]
            booking_links = [target for kind,target in page.links if kind=='a' and urlsplit(target).netloc=='www.trip.com']
            assert booking_links == [hotel['url']], (path, 'individual affiliate link')
            title,intro,sections=editorial(hotel,lang)
            schema=next(schema for schema in page.schemas if schema.get('@type')=='BlogPosting')
            assert schema['headline']==title and schema['description']==intro and 'citation' not in schema, (path,'source content metadata')
            if lang=='en':
                assert schema['headline']==hotel['seo_title_en'], (path,'source SEO title')
            text=(ROOT/path).read_text(encoding='utf-8')
            assert 'Bookdeal' not in text and 'docs.google.com/spreadsheets' not in text and 'downloads/' not in text, (path,'hidden spreadsheet details')
            assert escape(intro) in text and all(escape(paragraph) in text for _,paragraph in sections), (path,'editorial body')
    with (EXPORT_ROOT/'bookdeal-posts/posts.csv').open(encoding='utf-8-sig',newline='') as file:
        exported=list(csv.DictReader(file))
    assert len(exported)==len(HOTELS)
    for row,hotel in zip(exported,HOTELS):
        assert row['trip_affiliate_link']==hotel['url'] and row['post_en']==hotel['social_post_en'] and row['blog_content_en']==hotel['blog_content_en'], hotel['name']
    with zipfile.ZipFile(EXPORT_ROOT/'bookdeal-posts-hd.zip') as archive:
        assert len([p for p in archive.namelist() if p.endswith('.png')]) == 42
        assert len([p for p in archive.namelist() if p.endswith('.md')]) == 126
        assert archive.testzip() is None
    for i, (_, slug) in enumerate(SLUGS):
        if slug not in ARTICLE_DETAILS:
            continue
        for lang in LANGUAGES:
            path = article(lang, i)
            page = pages[path]
            details = ARTICLE_DETAILS[slug]
            assert any(link == details['booking'] for _, link in page.links), (path, 'source booking link')
            text = (ROOT/path).read_text(encoding='utf-8')
            assert 'source-note' in text and '2089517209634869439' in text, (path, 'X attribution')
            assert any('2089517209634869439' in citation for schema in page.schemas for citation in schema.get('citation', [])), (path, 'source citation')
    for path, page in pages.items():
        for lang in LANGUAGES:
            target = page.alternates[lang].removeprefix(BASE)+'index.html'
            assert pages[target].lang == lang, (path, lang)
            assert pages[target].alternates[page.lang] == url(path), (path, 'reciprocal alternate', lang)
    sitemap = ET.parse(ROOT/'sitemap.xml')
    locations = [e.text for e in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    assert Counter(locations) == Counter(url(path) for path in paths), 'sitemap mismatch'
    print(f'PASS: {len(paths)} HTML pages, featured images, local links and anchors, {len(LANGUAGES)}-language navigation, reciprocal hreflang, no advertising iframes, structured data and sitemap.')


if __name__ == '__main__':
    check()
