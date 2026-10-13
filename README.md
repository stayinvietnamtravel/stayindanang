# Stay in Da Nang – Static Affiliate Site

Responsive static website for hotels, flights, tours, deals, destinations and blog.

## GitHub Pages setup
1. Create a **public** GitHub repository named `YOURUSERNAME.github.io` (or any repository for a project site).
2. Upload **the contents of this folder** to the repository root.
3. Go to **Settings → Pages → Build and deployment → Deploy from a branch → main / (root)**.
4. Visit `https://YOURUSERNAME.github.io/` after publishing. For project repositories, the site runs under a subpath and the current root-relative URLs need adapting; a username.github.io repository is recommended.
5. For custom domain: add `CNAME` containing `stayindanang.com`, configure DNS per GitHub Pages docs, and update the Pages custom domain setting. Do not set a CNAME until you own and configure the domain.

## Before going live
- Check GitHub Pages Terms and usage limits for commercial/affiliate sites. Consider Cloudflare Pages if the commercial-use restrictions are unsuitable.
- Replace demo imagery if rights or availability are uncertain; the homepage image uses a third-party Unsplash URL.
- Verify the Trip.com affiliate link and commission attribution in your partner dashboard.
- Set up your GA4/GTM ID and consent banner where legally required. No tracking ID is configured by default. `affiliate_click` events are pushed to dataLayer only.
- Complete legal notices, contact details and substantive original travel content.
- Update canonical URLs and sitemap if using a github.io address rather than stayindanang.com.
- Deal listings are editorial examples, not verified live promotions or prices.
