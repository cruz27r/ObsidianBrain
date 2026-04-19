---
tags: [project, dnd, discord-bot, planning, typescript]
status: planning
created: 2026-04-19
---

# DND DM Bot — Project Context

## Snapshot

- Repo: `/Users/itocruz/Desktop/Projects/DND-DM-Bot`
- GitHub: `https://github.com/cruz27r/DND-DM-Bot`
- Purpose: Discord bot for D&D sessions that records voice chat, transcribes sessions, and generates campaign-aware summaries
- Intended stack: Node.js, TypeScript, discord.js, Deepgram, Anthropic, SQLite
- Current branch: `main`
- Current state: planning-stage repo with design spec pushed; implementation not started yet

## Existing Planning Context

- Main design note:
  - `docs/superpowers/specs/2026-03-26-dnd-scribe-bot-design.md`
- Design direction includes:
  - voice channel recording in chunks
  - Deepgram diarized transcription with timestamps
  - Claude-generated session summaries using campaign memory
  - SQLite-backed campaign/session library
  - slash commands for recording, sessions, and campaign metadata

## Recent Work

- Added and pushed the design spec to the repo
- Current pushed commit: `1eb0c8d` — `docs: add DND scribe bot design spec`

## Next Useful Actions

- Convert design spec into initial source scaffolding when implementation starts
- Add `package.json`, `tsconfig.json`, `.env.example`, and initial `src/` layout

## Related

- [[Desktop Projects Repo Map]]
