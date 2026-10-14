# Stay in Da Nang — One-page Landing Website

Website: https://stayinvietnamtravel.github.io/stayindanang/

## Install
1. Extract ZIP.
2. Open https://github.com/stayinvietnamtravel/stayindanang
3. Upload `index.html`, `.nojekyll`, `robots.txt`, `sitemap.xml` into the **root** of the repository.
4. Commit to `main`; enable Settings > Pages > Deploy from branch `main` / (root).
5. Hard refresh with Ctrl+Shift+R.

The website uses shared CSS and JavaScript under `assets/`. Upload the complete repository, including all language and blog directories, rather than only `index.html`. Links use relative paths and work with the GitHub Pages `/stayindanang/` base path.

## Languages and blog

English remains at the root. Localized landing pages and blog articles are available in Vietnamese (`vi`), simplified Chinese (`zh`), Russian (`ru`), Korean (`ko`), Japanese (`ja`) and Hindi (`hi`). Hindi is one language used in India, not a translation into every Indian language. Language links on a blog article open the equivalent article in the selected language. Translations are editorial drafts and may benefit from native-speaker review.

```text
assets/                         Shared styles and browser behavior
index.html                      English landing page
vi/ zh/ ru/ ko/ ja/ hi/         Localized landing pages
blog/
  index.html                    English blog index
  vi/ zh/ ru/ ko/ ja/ hi/       Localized blog indexes
  <en|vi|zh|ru|ko|ja|hi>/
    tips/vietnam-travel-planning/index.html
    hotels/where-to-stay-in-da-nang/index.html
    tours/da-nang-hoi-an-hue/index.html
    destinations/vietnam-heritage-guide/index.html
    tips/da-nang-hotels-tours-flights-2026/index.html
scripts/
  content.py                    Translations and official reference links
  x_post.py                     Expanded guide based on the owner-supplied X post
  build_site.py                 Static page and sitemap generator
  check_site.py                 Dependency-free structural checks
```

The blog covers real places and practical planning, with links to Vietnam Tourism, Vietnam Immigration and UNESCO. It does not claim first-hand visits, hotel ratings, live prices or guaranteed tour schedules. Generic landing-page photos remain illustrative. The article text and official reference links should be rechecked when entry rules or destination operations change.

The Da Nang 2026 hotel/tour/flight guide is based on the text of [this @stayindanang X post](https://x.com/stayindanang/status/2089517209634869439) supplied by the owner. The original post could not be fetched in the cloud environment. Its Trip.com link (`https://www.trip.com/t/ntD1RotVvV2`) is used for this guide's booking button, and the original post is cited on all seven translations. Promotional claims about ratings, cheap flights and exclusive prices are not treated as verified facts. No publication date is inferred from the X status ID.

## Local development

From the repository root, with Python 3 installed:

```sh
python3 scripts/build_site.py
python3 scripts/check_site.py
python3 -m http.server 8000 --bind 127.0.0.1
```

No package installation or build service is required for deployment: generated HTML is committed alongside the generator. Edit `scripts/content.py` or the sourced guide in `scripts/x_post.py` and run the generator to update localized pages, blog pages and `sitemap.xml`. The English landing page is maintained directly except for its blog-card section, which the generator refreshes. Shared files in `assets/` are maintained directly.

## Trip.com banners

Three affiliate banner IDs are included: `S14984461` (900×200), `SB20219796` (300×250), and `DB13678212` (250×250). The supplied Allianceid, SID and trip_sub1 values are preserved. `S14984461` appears once as the prominent hotel-search partner frame on each landing page and blog index. Its actual content and search capabilities are supplied by Trip.com; the site does not implement or promise a separate native search engine. On small screens, this 900-pixel frame scrolls horizontally inside its container to preserve readable controls. The two smaller banners scale to fit. Frames have accessible titles and an affiliate disclosure, and include a direct link if the external content does not load. Their content and language are controlled by Trip.com, not by the site's language selector. Do not apply a restrictive iframe sandbox without checking Trip.com's requirements, as it may break their ads.

All booking CTAs open the general Trip.com affiliate URL. Specific hotel/tour deep links are not configured. Photos load remotely from Unsplash, so internet access is required for them; use appropriately licensed, verified location images before commercial publication.

The website does not offer live pricing, booking forms or direct transactions.
Review GitHub Pages' limitations for primarily commercial sites; Cloudflare Pages is a potential alternative.
