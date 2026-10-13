# Stay in Da Nang – Travel Affiliate Website

## Deploy
This package targets https://stayinvietnamtravel.github.io/stayindanang/

1. Extract the ZIP.
2. Upload all files and folders (not the ZIP) to the root of https://github.com/stayinvietnamtravel/stayindanang
3. Commit to main.
4. GitHub repository Settings > Pages > Deploy from branch > main > /(root).
5. Hard refresh browser (Ctrl+Shift+R).

## Pages
Home, Hotels, Flights, Tours, Deals, Destinations, Blog, About, Privacy.

## Affiliate
All booking CTAs link to https://www.trip.com/t/Ygo40EEhzV2 with rel=sponsored. Links are generic: specific hotel/tour deep links need to be created in Trip.com Affiliate dashboard.

## Important
- The search-style widget opens the generic affiliate link, it does NOT transmit location, dates or travelers.
- Photos use remote Unsplash URLs; replace with verified licensed destination photographs.
- CSS is in assets/style.css. Do not omit the assets directory.
- Google Analytics is not enabled; affiliate click events are pushed to dataLayer for future GTM integration.
- Review GitHub Pages restrictions on primarily commercial sites. Cloudflare Pages may be a better long-term host for affiliate business.
- This is a new design inspired by common travel-site patterns, not an exact copy of the referenced website.
