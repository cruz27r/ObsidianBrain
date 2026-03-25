## Working Rules
- Prefer the smallest useful change.
- Match existing project patterns before inventing new ones.
- Keep scope tight unless user asks to expand.
- Show concrete verification before claiming success.
- If a skill is risky (browser automation, external APIs), ask before running broad actions.
- Keep shared agent tooling and reusable skill ports outside project repos unless the repo truly owns them.
- **Visual verification**: never claim a UI change is live without instructing the user to hard-refresh (Cmd+Shift+R). Dev servers and CDNs cache aggressively.
- **Social media images**: Instagram, Facebook, Yelp, and TikTok block all automated image access (JS-rendered, auth-gated). Flag this immediately; do not attempt scraping. Instruct the user to download manually.
- **Static file cache-busting (Next.js / frameworks)**: when swapping a static asset, delete the framework's cache dir (`.next/`, `.nuxt/`, etc.) AND rename the file to change its URL. Instruct user to hard-refresh after restart. Do not claim the change is visible until this full sequence is done.
