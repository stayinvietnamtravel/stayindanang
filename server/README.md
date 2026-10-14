# Deploy the travel assistant and private IP statistics

GitHub Pages cannot run AI requests or store visitor IPs. The website initially uses its clearly labelled automated travel guide. AI and IP recording remain disabled until this Worker is deployed and its public URL is configured. No API key belongs in the repository or browser.

1. In your Cloudflare account, install/use Wrangler 4.151.0 and log in:
   ```sh
   npx wrangler@4.151.0 login
   npx wrangler@4.151.0 d1 create stayindanang-analytics
   ```
2. Put the returned `database_id` into `server/wrangler.jsonc`. From `server/`:
   ```sh
   npx wrangler@4.151.0 d1 migrations apply stayindanang-analytics --remote
   npx wrangler@4.151.0 secret put OPENAI_API_KEY
   npx wrangler@4.151.0 secret put ADMIN_TOKEN
   ```
   Set a random admin token of at least 32 characters (prefer 32 random bytes). Keep it in your password manager. Do not paste credentials into chat, commit them, or put them in public configuration. `OPENAI_MODEL` defaults to `gpt-4.1-mini` and can be changed in the Worker configuration.
3. Deploy:
   ```sh
   npx wrangler@4.151.0 deploy
   ```
4. Set `data/assistant_config.json` → `backend_url` to the returned HTTPS Worker origin, without a path. Rebuild/check and publish:
   ```sh
   python3 scripts/build_site.py
   python3 scripts/check_site.py
   ```

The deployed Worker only accepts the configured website Origin. If moving to a custom website domain, change `ALLOWED_ORIGIN` and the allowlisted `KNOWLEDGE_URL` validation in `worker.mjs` together. CORS is not user authentication; public chat also has per-IP and global daily limits. The public API allows only 10 chat requests/IP/minute and 200 globally/day. Increase these consciously with your provider budget. OpenAI receives the user's message, up to six previous turns and curated public travel context; `store:false` is sent. Provider processing/retention policies still apply. The site does not log chat messages to its analytics database.

`/public-stats` returns only aggregate visits for the last 7 days. `/stats` requires the private admin token in the Authorization header and returns at most 100 IP rows. The token is not embedded in HTML, saved in browser storage, or sent as a URL parameter. Visitor IPs are read from Cloudflare's `CF-Connecting-IP` header only after the visitor explicitly enables analytics; they are not taken from user input. Query strings, referrers, chat text and browser identifiers are not stored. One visit per IP per UTC day is counted; shared networks and proxies mean this is not a count of unique people. A visitor can disable future logging from the footer. Records older than 7 days are excluded from all reads, deleted on writes/admin reads, and cleaned hourly by a scheduled task. Consent state and daily deduplication are stored only in the visitor's browser. Stopping collection does not erase previously collected records; those expire under the retention policy.

The IP-hash rate-limit table also processes the request IP for abuse prevention, independently of analytics consent. It stores salted hashes, not raw IPs, with minute/day buckets and a maximum two-day TTL; hourly cleanup removes expired buckets. Cloudflare and OpenAI are separate processors and can have their own service logs. Worker application observability is disabled in this template to avoid recording chat payloads or authorization headers.

The model cannot choose arbitrary links: responses use a strict JSON schema, and the server maps its service/property choice to the supplied affiliate allowlist. Exact property links are returned only for named properties in the Da Nang context. Unknown prices, ratings, visas, operating hours and amenities must be referred to the provider or official sources. Weather context is refreshed from the site's published knowledge file; a model answer is not a replacement for official local warnings.

Run backend checks with `node --test server/worker.test.mjs`.

## GitHub Actions deployment (recommended)

In repository **Settings → Secrets and variables → Actions**, add repository variable `CLOUDFLARE_ACCOUNT_ID` and secrets `CLOUDFLARE_API_TOKEN`, `OPENAI_API_KEY`, `ASSISTANT_ADMIN_TOKEN` (at least 32 random characters). The Cloudflare token needs Workers Scripts Edit (including account subdomain management) and D1 Edit for the selected account. Use a restricted token for this account, not your global API key. In **Actions**, run **Deploy AI assistant and private analytics**. The workflow configures/reuses the named D1 database, registers a Workers.dev subdomain if absent, deploys the pinned Wrangler version, stores secrets, verifies health and publishes the public backend URL to the site. It never writes the API keys or admin token to committed files. Existing database tables/data are preserved by the initial migration. Keep your admin token to view IP statistics in the website footer. If setup/deployment fails, the website remains in automatic-guide mode until a healthy backend is connected.
