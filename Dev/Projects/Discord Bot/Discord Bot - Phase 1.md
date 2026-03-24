---
tags: [project, planning]
status: planning
created: 2026-03-21
priority: medium
tech: [discord.js, typescript, anthropic-sdk, openai-sdk, replicate]
linked: []
---

# Discord Bot - Phase 1: Core + AI Commands

## Goal
Personal Discord bot with AI commands (Claude + GPT-4o), image generation (Flux Schnell), and GIF search — runs locally on demand, no always-on process.

## Decisions Locked In
- **Framework:** discord.js v14 + TypeScript
- **Language:** TypeScript (type safety for 3 AI provider APIs)
- **Project path:** `~/Desktop/CodeMSC/discord-bot/`
- **Local only:** run with `npx ts-node src/index.ts`, stop when done — no always-on process
- **No database for MVP:** thread message history = conversation context (stateless)

## Commands — Phase 1 Scope

| Command | What it does | API |
|---|---|---|
| `/askclaude [prompt]` | Ask Claude, reply in thread | Anthropic SDK |
| `/askcodex [prompt]` | Ask OpenAI GPT-4o, reply in thread | OpenAI SDK |
| `/imagine [prompt]` | Generate image with Flux Schnell + action buttons | Replicate API |
| `/gif [search]` | Return matching GIF | Tenor API (free) |
| `/ping` | Bot health check | None |
| `/help` | List all commands | None |

## Architecture

```
discord-bot/
├── src/
│   ├── commands/
│   │   ├── ai/
│   │   │   ├── askclaude.ts
│   │   │   └── askcodex.ts
│   │   ├── media/
│   │   │   ├── imagine.ts
│   │   │   └── gif.ts
│   │   └── util/
│   │       ├── ping.ts
│   │       └── help.ts
│   ├── events/
│   │   ├── ready.ts
│   │   └── interactionCreate.ts
│   ├── components/
│   │   └── buttons/
│   │       └── imagineActions.ts  (U1-U4 upscale buttons)
│   └── utils/
│       ├── anthropic.ts
│       ├── openai.ts
│       └── replicate.ts
├── deploy-commands.ts
├── .env
├── .env.example
├── package.json
└── tsconfig.json
```

## Key UX Patterns
- `interaction.deferReply()` is first line of every AI command (Discord 3s timeout)
- Each `/askclaude` or `/askcodex` starts a Discord thread — conversation continues there
- After `/imagine`, post image with 4 action buttons (Upscale 1-4) in an ActionRow
- Channel allowlist: AI commands only fire in channels listed in config

## Env Vars Needed
```
DISCORD_TOKEN=
DISCORD_CLIENT_ID=
ANTHROPIC_API_KEY=
OPENAI_API_KEY=
REPLICATE_API_TOKEN=
TENOR_API_KEY=
```

## Phases

- [ ] **Phase 1** — Core + AI commands (this note)
- [ ] **Phase 2** — Games (blackjack, trivia, dice RPG, mini-games)
- [ ] **Phase 3** — DnD tools (voice → Whisper → Claude summary → Obsidian note)
- [ ] **Phase 4** — Clothing brand bot (Shopify notifications, drops, customer DMs)

## Start Commands
```bash
# One-time: register slash commands
npx ts-node src/deploy-commands.ts

# Start bot locally
npx ts-node src/index.ts
```

## Resources
- Repo: `~/Desktop/CodeMSC/discord-bot/`
- [[Templates/Project]]

---

## Setup Steps — Before First Run

### Step 1: Create a Discord Application
1. Go to https://discord.com/developers/applications
2. Click **New Application** → give it a name (e.g. "RafaBot")
3. Go to **Bot** tab → click **Add Bot**
4. Under **Token** → click **Reset Token** → copy it → save as `DISCORD_TOKEN` in `.env`
5. Copy **Application ID** from General Information → save as `DISCORD_CLIENT_ID` in `.env`
6. Under **Privileged Gateway Intents** → enable:
   - Server Members Intent
   - Message Content Intent
7. Go to **OAuth2 → URL Generator**:
   - Scopes: `bot`, `applications.commands`
   - Bot permissions: Send Messages, Create Public Threads, Embed Links, Attach Files, Use Slash Commands
8. Open the generated URL → add bot to your test server

### Step 2: Fill in `.env`
Copy `.env.example` → create `.env` → fill in all values:
```
DISCORD_TOKEN=           ← from Discord Developer Portal
DISCORD_CLIENT_ID=       ← Application ID from Developer Portal
ANTHROPIC_API_KEY=       ← from console.anthropic.com
OPENAI_API_KEY=          ← from platform.openai.com
REPLICATE_API_TOKEN=     ← from replicate.com/account
TENOR_API_KEY=           ← from tenor.com/developer (free, register app)
ALLOWED_CHANNEL_IDS=     ← comma-separated Discord channel IDs where AI commands fire
```

**Getting channel IDs in Discord:** Settings → Advanced → Enable Developer Mode → right-click any channel → Copy Channel ID

### Step 3: Register Slash Commands (one-time)
```bash
cd ~/Desktop/CodeMSC/discord-bot
npx ts-node deploy-commands.ts
```
Expected output: `Deploying 6 commands... Commands deployed.`
This registers `/askclaude`, `/askcodex`, `/imagine`, `/gif`, `/ping`, `/help` globally.

### Step 4: Run the Bot Locally
```bash
npx ts-node src/index.ts
```
Expected: `Ready! Logged in as RafaBot#1234`

Stop with `Ctrl+C` when done — no background process needed.

### Step 5: Test in Discord
- `/ping` → should reply with latency
- `/help` → should show embed with all commands
- `/askclaude hello` → should defer then reply (takes 2-5s)
- `/imagine a red ferrari` → should generate image + show U1-U4 buttons
- `/gif dog` → should return a GIF URL

---

## Scaffold Status
- Scaffold created at `~/Desktop/CodeMSC/discord-bot/` on 2026-03-21
- All source files written, `npm install` complete, TypeScript compiles clean
- Waiting on: Discord app creation + `.env` values

## Notes
- 2026-03-21: Phase 1 planned and scaffolded. Full TypeScript project at `~/Desktop/CodeMSC/discord-bot/`. All commands coded. Blocked on Discord app setup + API keys.
