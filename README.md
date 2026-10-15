# Stay in Da Nang — Multilingual Vietnam Travel Website

Website: https://stayinvietnamtravel.github.io/stayindanang/

## Install
1. Extract ZIP.
2. Open https://github.com/stayinvietnamtravel/stayindanang
3. Upload the complete site, including `assets/`, language and `blog/` directories, `.nojekyll`, `robots.txt` and `sitemap.xml` into the **root** of the repository.
4. Commit to `main`; enable Settings > Pages > Deploy from branch `main` / (root).
5. Hard refresh with Ctrl+Shift+R.

The website uses shared CSS and JavaScript under `assets/`. Upload the complete repository, including all language and blog directories, rather than only `index.html`. Links use relative paths and work with the GitHub Pages `/stayindanang/` base path.

## Languages and blog

English remains at the root. The site supports 13 language editions: English, Vietnamese (`vi`), simplified Chinese (`zh`), traditional Chinese (`zh-Hant`), Russian (`ru`), Korean (`ko`), Japanese (`ja`), Hindi (`hi`), French (`fr`), German (`de`), Spanish (`es`), Thai (`th`) and Indonesian (`id`). Hindi is one language used in India, not a translation into every Indian language. A compact language picker opens the equivalent article in the selected language. Translations are editorial drafts and may benefit from native-speaker review.

There are eight editorial topics in every language: planning, hotel areas, a Central Vietnam itinerary, heritage destinations, the source-based Da Nang 2026 guide, regional food, coastal experiences and city walks. These produce 104 guide pages. A separate hotel-picks section adds 42 hotels in 13 language editions and 13 indexes. International resource/news pages add 26 pages, bringing the site to 715 HTML pages. The category buttons filter blog cards by tips, hotels, routes, destinations, food or experiences; all cards remain available without JavaScript.

```text
assets/                         Shared styles and browser behavior
  blog/                         Eight original local SVG cover illustrations
  hotel-deals/                  42 HD typographic PNG cards, 1600 × 900
index.html                      English landing page
<language>/                    Localized landing pages (12 editions)
blog/
  index.html                    English blog index
  <language>/                  Localized blog indexes
  <en|vi|zh|zh-Hant|ru|ko|ja|hi|fr|de|es|th|id>/
    tips/vietnam-travel-planning/index.html
    hotels/where-to-stay-in-da-nang/index.html
    tours/da-nang-hoi-an-hue/index.html
    destinations/vietnam-heritage-guide/index.html
    tips/da-nang-hotels-tours-flights-2026/index.html
    food/vietnam-food-guide/index.html
    experiences/coastal-vietnam-experiences/index.html
    destinations/hanoi-ho-chi-minh-city-walks/index.html
deals/<language>/              Top Deals / Hot Sellers index and hotel posts
resources/<language>/          International tourism sites and travel magazines
news/<language>/               Attributed international travel headlines
data/bookdeal.json             Extracted hotel names, links and source provenance
data/travel_sources.json       Tourism references, publications and RSS configuration
data/travel_news.json          Fetched headlines, source status and actual timestamps
data/weather.json              Attributed MET Norway forecasts for five destinations
scripts/
  content.py                    Translations and official reference links
  x_post.py                     Expanded guide based on the owner-supplied X post
  extra_locales.py              Six additional translated editions
  extra_topics.py               Food, coastal experiences and city walks
  feature_images.py             Original SVG artwork generator
  deal_posts.py                 Bookdeal posts, hotel pages, exports and HD cards
  hotel_editorial.py            Translations of the workbook's blog themes
  import_bookdeal.py            Validated name/link/content spreadsheet importer
  travel_portal.py              International resources and news page generator
  refresh_travel_news.py        Safe RSS/Atom headline cache updater
  refresh_weather.py            Validated weather data cache updater
  home_tools.py                 Weather, trip ideas and checklist in 13 languages
.github/workflows/
  travel-news.yml               Scheduled headline refresh and Pages build request
  weather.yml                   Weather refresh every three hours
  build_site.py                 Static page and sitemap generator
  check_site.py                 Dependency-free structural checks
```

The blog covers real places and practical planning, with links to Vietnam Tourism, Vietnam Immigration and UNESCO. It does not claim first-hand visits, hotel ratings, live prices or guaranteed tour schedules. Generic landing-page photos remain illustrative. The article text and official reference links should be rechecked when entry rules or destination operations change.

The Da Nang 2026 hotel/tour/flight guide is based on the text of [this @stayindanang X post](https://x.com/stayindanang/status/2089517209634869439) supplied by the owner. The original post could not be fetched in the cloud environment. Its Trip.com link (`https://www.trip.com/t/ntD1RotVvV2`) is used for this guide's booking button, and the original post is cited on all 13 language editions. Promotional claims about ratings, cheap flights and exclusive prices are not treated as verified facts. No publication date is inferred from the X status ID.

Every article and blog card has a locally stored featured illustration. Each topic has its own original SVG cover, shared across translations with localized alternative text and an article caption identifying it as an illustration rather than a destination photograph. The artwork does not require external image services and is regenerated by the site build. The original landing page still uses illustrative remote photos.

## Bookdeal hotel posts

`data/bookdeal.json` records all 49 entries from the owner's latest `Bookdeal_Image_Automation_Ready (1).xlsx`, including source worksheet, row, workbook SHA-256, English SEO title, blog body, social post, CTA, keywords, hashtags and image metadata. The initial name/link source was `Bookdeal.xlsx`; the 49 names and booking URLs match between the two uploads. The original workbooks are not published. Forty-two entries are included: 23 Top Deals and 19 Hot Sellers. Seven explicitly Hoi An/An Bang entries are retained as excluded metadata. Shilla Monogram Danang is marked as being on the coastal Da Nang–Hoi An corridor so visitors can verify its exact location.

The latest workbook supplies English editorial and social content but no prices, discount percentages, ratings, sales counts, hotel photos or validity dates. All verified-image URL, photo source and photo attribution fields are empty; all image statuses are `Needs verified official image URL`. Creative briefs are stored as data and do not trigger image fetching or generation. Worksheet names are preserved as source categories, not confirmed live offers or popularity rankings. Each hotel page has exactly one Trip.com booking link, preserved byte-for-byte from the spreadsheet. Descriptive promotional suffixes in source names are not treated as verified amenities.

The English hotel edition uses the supplied SEO headline, introduction and comparison/travel-inspiration paragraphs, with the original URL rendered once as a booking button. The other 12 editions translate those themes: location, guest reviews, room photos, cancellation, breakfast, transport and time for My Khe, the Han River and Hoi An. The original English draft remains retained in the administrative export bundle. Updates preserve existing hotel slugs, affiliate links and HD artwork.

The administrative ZIP contains 42 updated Vietnamese social posts, 42 original English social posts, 42 English source blog drafts, a UTF-8 CSV with the original content fields and 42 short posts (at most 280 characters each), plus 42 original text-card PNGs at 1600 × 900. These are typographic designs, not property photographs. No social posts are automatically sent to X or other platforms. The 13 website editions share the Vietnamese artwork, with localized page text and alternative descriptions.

`python3 scripts/build_site.py` rebuilds the hotel pages and deterministic administrative bundle from the JSON and committed artwork using the standard library. To recreate the artwork itself, run `python3 scripts/deal_posts.py --render-images`; this optional command requires Playwright and Chromium at `/usr/bin/chromium`. The extractor used OpenPyXL only when reading the uploaded workbook; normal site builds do not need it.

To import another workbook using the same column headings, run `python3 scripts/import_bookdeal.py /path/to/file.xlsx` (requires OpenPyXL), then rebuild and check the site. The importer reads cached values without executing Excel formulas, validates each blog/social/CTA URL against the hotel's booking link, keeps existing slugs and exclusions, and rejects conflicting hyperlinks, duplicate identities or missing existing hotels. Input is validated before the JSON is replaced. Image URL presence alone is not proof of licensing or verification.

## International resources and news

The directory lists 18 official tourism destinations and 10 travel magazines/publications, including Vietnam Tourism, JNTO, Korea Tourism Organization, Tourism Thailand, Singapore Tourism Board, France.fr, VisitBritain, Condé Nast Traveler, Travel + Leisure, AFAR, GEO and Lonely Planet. These are outbound reference links, not claims of partnership or reciprocal backlinks. Destination and publication names retain their original branding; navigation and explanatory text have 13 language editions.

News pages render attributed headlines from TAT Newsroom, TTG Asia and TravelDailyNews International RSS feeds. Article bodies and publisher photographs are not copied. Dates come from the feed, never from the fetch time; absent dates are labelled as missing. Displayed times use Asia/Bangkok (+07:00). Headline destination tags use explicitly mentioned location names and the publisher's scope; headlines remain in their source language. Visitors can filter by destination and open the original publication. With no successful fetch, the page states that no headlines have been downloaded and provides direct publisher links instead.

Run `python3 scripts/refresh_travel_news.py` to refresh the cache, then rebuild and check the site. Only HTTPS article links on configured publisher hosts are accepted, duplicates are removed, dates more than 60 days old or over one hour in the future are rejected, and at most 12 items per publisher are retained. Missing publication dates remain null. TLS verification stays enabled. HTML/script markup and RSS instructions are treated as data; no commands from feeds are executed. A publisher failure preserves its existing cache. If every publisher fails, the command exits nonzero and does not claim a successful fetch.

The `Refresh travel news` GitHub Actions workflow runs on initial configuration push, manual dispatch and at 06:00/18:00 UTC (13:00/01:00 Asia/Bangkok), subject to GitHub scheduler timing. It uses only Python's standard library, rebuilds/validates the site and commits refreshed data with the platform token. Because token-based commits do not automatically trigger a GitHub Pages branch build, the workflow explicitly requests that build through the Pages API. It has `contents: write` and `pages: write` permissions, preserves normal fast-forward safeguards and never force-pushes. It assumes the documented `main / root` Pages deployment; it does not alter Pages settings.

The cloud task's first feed fetch was blocked by its network policy, so the initial cache contained no invented headlines. A successful build of the site alone does not establish that the scheduled workflow fetched feeds or that Pages published them; check the Actions run and Pages deployment for runtime status.

## Local development

From the repository root, with Python 3 installed:

```sh
python3 scripts/build_site.py
python3 scripts/check_site.py
python3 -m http.server 8000 --bind 127.0.0.1
```

No package installation or build service is required for deployment: generated HTML is committed alongside the generator. Edit the appropriate content module in `scripts/` and run the generator to update localized pages, blog pages, cover illustrations and `sitemap.xml`. The English landing page is maintained directly except for blog cards, language navigation, alternate-language metadata and the marked `HOME TOOLS` section, which the generator refreshes. Shared CSS and JavaScript in `assets/` are maintained directly.

## Homepage weather and new trip ideas

All 13 homepages include a five-destination forecast selector (Da Nang, Hanoi, Sa Pa, Ho Chi Minh City and Phu Quoc), localized food and experience suggestions, interactive 1/3/5-day trip ideas, rainy-day options and a three-item pre-travel checklist. The checklist stores only checkbox states in the visitor's browser and is shared between language editions on the same site; it works without persistence when browser storage is unavailable. The duration controls link to existing food, itinerary and heritage guides. They are planning suggestions, not guaranteed tours.

Forecast data comes from MET Norway's Locationforecast API for the fixed locations in `scripts/destinations.py`, with attribution and a CC BY 4.0 link. The panel displays five forecast points around the next 24 hours with Celsius temperature, wind in m/s and rainfall in mm with its actual forecast interval. These are model forecasts, not measured observations or rain probabilities. Dates are shown at +07:00. No visitor location, API key or browser-to-provider request is needed. Missing or stale model data shows a truthful unavailable state and a link to Yr.

Run `python3 scripts/refresh_weather.py` to fetch the forecast, then build and check the site. The updater identifies itself with the site's repository URL, preserves TLS checks, validates units and timestamps, rejects nonfinite or implausible measurements, and retains the previous cache on failure. The GitHub `Refresh Vietnam destination weather` workflow fetches every three hours, builds/checks, commits and requests the Pages branch build. Both content-update workflows share a concurrency group to avoid racing each other's commits. The initial cloud fetch was blocked by network policy; forecasts are only shown after a real successful fetch.

## Trip.com booking links

The three advertising iframes, including the hotel-search banner, have been removed from all pages and from the generator. The automated checks reject any reintroduced iframe or Trip.com ad URL. Booking buttons now point to the hotel's own supplied affiliate URL or to the original general booking link, depending on the page; the hotel links remain intact. There is no embedded booking engine.

The original English homepage photos load remotely from Unsplash; blog covers and HD text artwork are local files. Photos remain illustrative, and verified licensed property photographs still require source URLs and attribution.

The website does not offer live pricing, booking forms or direct transactions.
Review GitHub Pages' limitations for primarily commercial sites; Cloudflare Pages is a potential alternative.

Spreadsheet filenames, provenance captions, schema citations and export-download links are hidden from visitor pages. Export bundles are generated outside the repository at `../stayindanang-admin-exports/`; previously published downloads have been removed. Source provenance remains in the repository for editorial maintenance. This does not change the Google spreadsheet’s sharing permissions or make a public repository private. The selected forecast destination is saved locally in the browser; no coordinates or personal details are collected. Each city refresh is independent: failed requests retain that city’s previous cache while successful cities update.

## Discovery UI and affiliate routing

All 13 homepages share the booking selector, four-column discovery rails (swipeable on mobile), eight featured hotels, category filters and local favorites. Covers remain original editorial illustrations or hotel text artwork, not unverified property photos. No screenshot prices, star ratings, sales rankings, awards or coupon percentages are copied into the site.

`data/affiliate_routes.json` is the editable routing configuration. The owner's supplied service short links are preserved exactly: hotels, flights, tours/tickets, airport transfers and car rentals. `default_url` opens the general Trip.com homepage. Optional `routes` entries can override a service for an individual destination, for example `"hanoi": {"hotels": "<supplied Trip.com short link>"}`. Without a city-specific override, a service link opens that service on Trip.com; travelers then select the destination and dates there. No unsupported deep-link parameters are appended. The 42 property links come from the existing hotel data and take precedence when a specific Da Nang hotel is chosen. Switching away from Da Nang or away from hotels disables the property selector and uses the correct service route; it never retains a hidden property's booking target. The weather and booking destination selectors stay synchronized. Blog booking buttons use the relevant service, while the article based on the owner's X post retains its supplied source link.

Configuration is validated at build time to accept only HTTPS `www.trip.com/t/<id>` or `/w/<id>` links. Client routing uses the same allowlist and has usable static links when JavaScript is disabled. Favorites and selected destinations are stored only in the visitor's browser. Changes to routing require rebuilding and committing generated HTML.

## World destination selector

The booking panel offers continent, country and city filters across Asia, Europe, the Americas and Australia/Oceania. `scripts/world_destinations.py` maintains 36 countries and 101 city/destination options, including the existing Vietnamese destinations. Country labels use browser `Intl.DisplayNames` for the site's language, with English/Vietnamese static fallbacks; city names use curated labels. Filters preserve an existing city when it remains available and choose a valid city when it does not. The selected city is retained locally between visits. All destination options remain available in the static HTML when JavaScript is disabled.

International selections use the supplied service affiliate links, unless a specific city/service override is supplied in `data/affiliate_routes.json`. The destination is displayed in the booking summary; travelers choose it and their dates again on Trip.com because the supplied short links do not provide verified destination parameters. The weather panel remains limited to the five cached Vietnamese destinations. Selecting an international city keeps that forecast selector valid; selecting a Vietnamese forecast city restores the corresponding Vietnam booking selection. Da Nang's individual hotel links retain precedence over general hotel links.

## Worldwide weather and search discoverability

The forecast updater now covers all 101 curated destinations, with fixed coordinates and IANA timezones in `scripts/world_weather.py`. Four concurrent requests bound provider load and job duration; each city's failed refresh independently retains its previous data. The scheduler runs every three hours. Forecast cards display the destination's local time, including daylight-saving offsets where applicable; model-update timestamps retain the site's explicitly shown +07:00 time. City-center coordinates do not represent entire countries, islands or mountain regions. Missing or stale forecasts stay visibly unavailable. No visitor geolocation or API keys are used.

`explore/<language>/<region>/` adds 52 regional guides in 13 languages. Visible content includes itinerary examples, food ideas, country/city directories linking to the corresponding forecast, service-specific affiliate links and official tourism sources. Regional Article schemas include publisher, publication date, citations and geographic coverage; breadcrumb markup mirrors the displayed trail. Canonical and reciprocal language links include every guide in the sitemap. Organization/WebSite JSON-LD and Twitter share metadata cover every page; a local 1200×630 share image provides a fallback. `robots.txt` references the sitemap and avoids indexing administrative source directories. `llms.txt` is an optional reading index for guides and editorial boundaries; it does not guarantee crawler adoption, AI citations or rankings. We do not add unverified ratings, fake discounts, fabricated firsthand experiences or unsupported FAQ rich-result claims. Search Console/indexing submissions need the owner's account and were not performed.

## Travel chat and private visitor statistics

Every page includes a localized chat dialog and footer statistics in all 13 languages. The default is a clearly labelled automatic travel guide using curated planning FAQs and the supplied service/property affiliate links. It is not presented as a live AI model. Cloudflare AI and visitor logging remain disabled while `data/assistant_config.json.backend_url` is empty. There is no public IP lookup service, model key, administrator token or visitor IP list in website source.

The deployable backend is in `server/`. It uses OpenAI through a secret-bearing Worker and D1 for consented visit records. Public footers show aggregate counts; the individual IP list requires a private administrator token and is never publicly exposed. Visitors can accept, decline or disable analytics. IPs are kept under a seven-day retention policy; counts are one visit per IP per UTC day, not unique people. Chat messages are held only in memory on the website and are not saved in the analytics database.

See `server/README.md` for account setup, secret configuration and the manual **Deploy AI assistant and private analytics** workflow. That workflow deploys the backend, verifies health and only then connects the public website. Both recurring content workflows commit updated chat knowledge alongside weather/news pages so AI answers use the current public guide data. Backend tests run with `node --test server/worker.test.mjs`.

## Original AI travel images

`assets/ai-travel/` contains 18 original ChatGPT-generated HD illustrations: two text posters and sixteen destination/editorial scenes. Native HTML titles and AI attribution work in all 13 editions. HD PNG originals are preserved in the repository; browser images use responsive WebP. The standalone homepage artwork section has been removed, with images placed inside relevant blog and regional guides instead. Generic Da Nang hotel-area illustrations are not presented as photographs of individual properties.

`scripts/optimize_images.py` exports 270 responsive WebP variants from 90 originals, including 42 Da Nang and 30 Hanoi hotel text cards. New AI thumbnails are approximately 39–84 KB (median 56 KB), around 98% smaller than their PNG originals; this compares file sizes, not total page-load times. `scripts/responsive_images.py` supplies `srcset`, accurate dimensions and lazy loading, with priority loading for article covers. Normal builds read the committed image registry without Pillow; install Pillow only to export new artwork. Open Graph/Twitter retain the HD covers.

## Hanoi hotel guides

`data/hanoi_hotels.json` stores 30 distinct Hanoi hotels and all 31 supplied Trip.com affiliate URLs. Aurora Premium appears twice in the workbook; one article preserves both links. Existing Da Nang records and URLs are retained. `scripts/import_hanoi_hotels.py <workbook.xlsx>` reads only the two Hanoi tabs as data, validates HTTPS Trip.com short links and matching cell hyperlinks, and records source rows. No spreadsheet instructions or formulas are executed. Import requires openpyxl.

`blog/<language>/destinations/hanoi/` contains the destination index and `hotels/<slug>/` contains each guide in all 13 languages. Vietnamese guides contain individual editorial angles; other editions use localized room-comparison and Hanoi itinerary guidance. Articles avoid unsupported amenities, prices, rankings and proximity claims. Blog/homepage and Deals callouts link to Hanoi, and the booking selector filters property names by city. The chatbot links to the correct Hanoi guide path.

Run `python3 scripts/hanoi_hotels.py` to render 30 exact-name HD text designs (Playwright/Chromium), then `python3 scripts/optimize_images.py` to export lightweight WebP variants. Regular builds reuse the committed images. Each card includes its own hotel name, Hanoi label and supplied affiliate URL(s); these are typographic designs, not property photographs.
