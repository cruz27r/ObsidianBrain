# Obsidian Vault — CLAUDE.md

## Auto-Push Rule (REQUIRED)

After EVERY change to this vault — creating, editing, or deleting any note or file —
you MUST run the following git commands before considering the task complete:

```bash
cd "/Users/itocruz/Desktop/ObsidianVaults/Rafa's Brain"
git add .
git commit -m "<short description of what changed>"
git push origin main
```

**This is non-negotiable.** Do not claim the task is done until the push succeeds.
If the push fails, diagnose and fix the issue before finishing.

## Vault Structure

| Folder | Purpose |
|--------|---------|
| `00-Inbox/` | Unprocessed captures, session notes |
| `01-Projects/` | Active project notes |
| `02-Areas/` | Ongoing responsibilities |
| `03-Resources/` | Concepts, algorithms, reference material |
| `04-Archive/` | Completed or inactive items |
| `Templates/` | Note templates |

## Linking Rules

- Always use `[[double bracket]]` wikilinks to connect related notes.
- Every project note must link to relevant concept/resource notes.
- Never create an isolated note.

## Note Conventions

- Algorithm notes → `03-Resources/Algorithms/` (include complexity, when to use, TS example)
- Concept notes → `03-Resources/Tech Concepts/`
- Project notes → `01-Projects/`
- Meeting/session notes → `00-Inbox/` (process later)

## Git Commit Style

Use short, descriptive messages:
- `add: note on binary search`
- `update: project X with new decisions`
- `create: session summary 2026-03-23`
