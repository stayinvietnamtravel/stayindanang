# Connect the 30-day campaign

The website and campaign assets work on GitHub Pages. Social publishing runs on GitHub Actions because the static website cannot safely store account tokens. The owner requested one topic each day on X, Facebook and Instagram. The prepared schedule is **09:00 Asia/Bangkok (UTC+7)**, for 30 campaign days, starting on the date configured below.

Current state: content and integration code are prepared; live account authorization has not been established in this workspace. No posts have been sent. A profile URL alone does not provide API access. Do not paste credentials in chat, CSV files, website JavaScript or this repository.

## Account requirements

- X: an X developer app with user-context Read and Write access and API/media-upload access supported by the account's current API plan. The publisher uses OAuth 1.0a user credentials, `GET /2/users/me`, `POST /2/media/upload`, and `POST /2/tweets` on `api.x.com`.
- Facebook: a **Facebook Page**, not a personal profile, with a Page access token authorized for the relevant publishing operations, such as `pages_manage_posts` and applicable page-read permissions. The account ID must be `61594990174326`. If the supplied profile URL represents a personal account, this API workflow cannot publish to it; provide an authorized Page and update the expected ID instead.
- Instagram: a professional account linked to that Page, with the necessary Instagram read/content-publishing permissions. The configured username must be `stayindananghoianhue`. This implementation uses the Instagram API with Facebook Login; the alternative Instagram Login flow is not implemented. Meta app review/access requirements depend on account roles and deployment mode.

Review [X API documentation](https://docs.x.com/x-api) and Meta documentation for [Facebook Page posts](https://developers.facebook.com/docs/pages-api/posts/) and [Instagram publishing with Facebook Login](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-facebook-login/content-publishing/) for current permissions and API entitlement. Provider identity checks run before any public publishing request. They must match `social/publishing.json`; the workflow never silently publishes to a different account.

## Configure GitHub securely

Open this repository's **Settings → Secrets and variables → Actions** and create these repository secrets:

| Secret | Value supplied securely by the owner |
| --- | --- |
| `X_API_KEY` | X app consumer/API key |
| `X_API_SECRET` | X app consumer/API secret |
| `X_ACCESS_TOKEN` | User access token for `@stayindanang` |
| `X_ACCESS_TOKEN_SECRET` | Matching user access-token secret |
| `META_PAGE_ACCESS_TOKEN` | Authorized token for the configured Facebook Page and linked Instagram account |

For an X app whose access was upgraded, generate credentials with the required publishing scope. Keep token expiry/revocation in mind for Meta as well; this repository does not manage OAuth login or automatically refresh expired tokens. Meta API version is explicitly configurable in `social/publishing.json` (initially `v24.0`).

Then use **Actions → Publish daily travel campaign → Run workflow**:

1. Run `preview` for day 1. This performs local validation and shows prepared captions/asset paths; it sends no API requests.
2. Run `verify-accounts` for all platforms. This uses read-only API calls to confirm the expected X username, Facebook Page ID and linked Instagram username.
3. Once the website and JPEG URLs have deployed, configure repository variables `SOCIAL_START_DATE` (local calendar date, `YYYY-MM-DD`) and `SOCIAL_AUTO_PUBLISH=true` to begin daily publication. Do not choose a start date already in the past unless intentionally starting at a later campaign day. Leave the flag unset/false to keep automation disabled.

The cron trigger runs at 02:00 UTC, which is 09:00 in Vietnam/Thailand. GitHub schedules may be delayed and are not a guaranteed exact-time service. A manual `publish` run is also available for a selected day/platform. Previously confirmed posts are skipped; do not manually publish day 1 and expect a second day-1 post when the schedule starts.

## Content and images

`data/social_campaign.json` retains all 150 original drafts and 30 prompt rows as data. The generated `social/outbox.json` contains the 90 prepared X/Facebook/Instagram posts. TikTok and Pinterest were not authorized as publishing destinations and remain source drafts only. Blog links point to the matching English article and retain platform-specific UTM attribution. Service affiliate destinations are normalized to the owner's existing approved links; rail/general-planning topics use the general link and clearly require further selection.

Every topic has an original AI poster plus responsive web derivatives. Social uploads use JPEGs preserving the complete poster without cropping its text; the generated dimensions are in the outbox. Instagram uses a supported photo aspect ratio, which can differ from the portrait-carousel concept in the input file. AI and affiliate disclosures are included in the prepared captions. Image URLs in the outbox must be publicly reachable after GitHub Pages deployment; Instagram and Facebook cannot fetch a local workspace file.

To regenerate after editing the source CSVs or artwork:

```sh
python3 scripts/import_social_campaign.py posts.csv prompts.csv
python3 scripts/optimize_images.py
python3 scripts/export_social_campaign.py
python3 scripts/build_site.py
python3 scripts/check_site.py
python3 -m unittest discover -s tests -p 'test_social_publishing.py'
python3 scripts/publish_social.py --day 1
```

Pillow is needed for image export and the offline asset-validation tests. Normal HTML builds and the publisher use Python's standard library. The private review ZIP is written outside the public repository to `../stayindanang-admin-exports/social-campaign-30days.zip` and includes the 90 captions/JPEGs and all 150 original drafts.

## Reliability and recovery

`data/social_publications.json` stores one result per campaign day/platform. Workflow concurrency prevents overlapping publisher jobs. Confirmed publication IDs are recorded; they are not sent again on a retry. A crash or timeout after a publishing request creates a `publishing`/`uncertain` entry and **blocks automatic retries** for that entry to avoid duplicate public posts. Inspect the actual account before deciding whether to mark it published with its ID or clear an unpublished attempt. Only known API rejections are treated as retryable failures. Do not delete a confirmed ledger entry to force another post.

The workflow commits the ledger even when an API request fails and also uploads an artifact. If ledger persistence fails, restore the artifact and review public accounts before retrying. Enable/disable the schedule using `SOCIAL_AUTO_PUBLISH`; no live social job runs just because website content was pushed.
