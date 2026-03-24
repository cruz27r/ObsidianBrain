# Global CLAUDE.md

<!-- CARL-MANAGED: Do not remove this section -->
## CARL Integration

Follow all rules in <carl-rules> blocks from system-reminders.
These are dynamically injected based on context and MUST be obeyed.
<!-- END CARL-MANAGED -->

## Core Workflow
- Keep this file lean; dynamic behavior should come from CARL domains.
- Start with `using-superpowers` each session.
- Multi-step work: `writing-plans`.
- Implementation: `test-driven-development`.
- Debugging/regressions: `systematic-debugging`.
- Completion: `verification-before-completion` then `requesting-code-review`.

## Skill Routing (Simple)
- Frontend/UI work: use `frontend-design`.
- Browser QA or flow automation: use `playwright`.
- Files like PDF/DOCX/PPTX/XLSX: use `document-skills`.
- MCP/server integration work: use `mcp-builder`.
- Google Workspace ops: use `gws` (mail/calendar/drive/docs/sheets).
- Browser agent tasks: use `browser-use` MCP only when explicitly needed.
- Market/web research APIs: use `valyu-mcp` only when key is configured.
- Design system generation: use `theme-factory`.
- Brand consistency checks/content: use `brand-guidelines`.
- Creative visual generation: use `algorithmic-art`.
- Social/comms GIF generation: use `slack-gif-creator`.
- External second-opinion review: use `codex-review`.
- Codex CLI delegation: use `codex` (from `skill-codex`) for deep review/audit or parallel analysis.
- Image processing (logo bg removal, format conversion, resizing): Python/Pillow via a throwaway venv (`/tmp/imgenv`).
- Live library docs in context: use `context7` MCP — prevents stale API hallucinations.
- Architecture diagrams / whiteboarding: use `excalidraw` MCP.
- Cross-session memory: `claude-mem` plugin — auto-injects relevant prior context.
- GitHub operations (repos, PRs, issues, Actions): use `github` MCP.
- AI-native web/code/docs search: use `exa` MCP.
- Full-stack backend (DB, auth, storage, edge functions): use `supabase` MCP.
- Payments, billing, subscriptions: use `stripe` MCP.
- PDF read/extract: use `pdf-reader` MCP.
- Word document creation/editing: use `office-word` MCP.
- Google Docs/Sheets/Slides/Forms (multi-account): use `google-workspace` MCP (taylorwilsdon).
- Notion read/write: use `notion` MCP + Notion Claude Code plugin.
- Obsidian vault read/write/search: use `obsidian` MCP (requires Local REST API plugin in Obsidian).
- Shopify Admin API: use `shopify` MCP + `shopify-dev` MCP for docs/schema.
- Print-on-demand products: use `printify` MCP.
- Mobile app testing (iOS/Android): use `appium` MCP.
- Zoom meeting transcripts → notes: use `zoom_transcript_mcp` (requires manual clone + build).

## CARL Auto-Domains (keyword-triggered)
These inject automatically when relevant keywords appear — no manual invocation needed:
- **SHOPIFY**: shopify, liquid, storefront, polaris, myshopify
- **GAMING**: unity, godot, phaser, three.js, minecraft mod, webgl, game dev
- **NOTES**: obsidian, notion, zoom notes, meeting notes, transcript, vault
- **CLOTHING-BRAND**: clothing brand, merch, printify, hoodie, apparel, brand identity
- **BOTS**: discord bot, slack bot, discord.js, bolt sdk, slash command
- **DOCUMENTS**: pdf, word doc, docx, excel, xlsx, powerpoint, google docs/sheets/slides

## Context Efficiency
- Default to concise responses focused on outcomes.
- Avoid repeating already-known context in the same session.
- Prefer CARL triggered domains over static repeated instructions.
- Summarize command/test output instead of dumping raw output.
- Keep intermediate notes ephemeral; keep only actionable conclusions.
- If a tool emits long output, extract only high-signal lines and discard the rest.

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
