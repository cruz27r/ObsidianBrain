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
| `00-Inbox/` | Raw captures, quick notes, unprocessed ideas |
| `Dev/` | Active coding & engineering projects |
| `Gaming/` | Game dev, modding (Minecraft etc.), engines |
| `School/` | Courses, assignments, study notes |
| `Knowledge/` | The dictionary — all reference & concept material |
| `Business/` | Personal ventures (clothing brand, web agency, clients) |
| `Career/` | Job applications, resume, interview prep |
| `Claude Setup/` | Skills, CARL domains, settings — synced backup |
| `Archive/` | Completed or inactive items |
| `Templates/` | Note templates |

## Where Does It Go? (Routing Rules)

- **Building or working on something?** → its domain folder (`Dev/Projects/`, `Gaming/Projects/`, `Business/`)
- **Looking something up / reference?** → `Knowledge/`
- **School work?** → `School/`
- **Business venture or client?** → `Business/`
- **Career / job related?** → `Career/`
- **Something just came in?** → `00-Inbox/`

## Note Conventions

- Algorithm notes → `Knowledge/Algorithms/` (include complexity, when to use, TS example)
- Concept/tech notes → `Knowledge/Tech Concepts/`
- Dev projects → `Dev/Projects/<project-name>/`
- Game modding → `Gaming/Modding/<game>/`
- Meeting/session notes → `00-Inbox/` (process later)

## Claude Setup Auto-Sync Rule (REQUIRED)

Whenever any of the following happen, you MUST mirror the files to this vault and push:

**Skills installed or updated:**
```bash
cp ~/.claude/plugins/cache/superpowers-dev/superpowers/5.0.5/skills/<skill>/SKILL.md \
   "/Users/itocruz/Desktop/ObsidianVaults/Rafa's Brain/Claude Setup/Skills/<skill>.md"
```

**CARL domains added or edited:**
```bash
cp <path-to>.carl \
   "/Users/itocruz/Desktop/ObsidianVaults/Rafa's Brain/Claude Setup/CARL Domains/"
```

**Global CLAUDE.md or settings.json changed:**
```bash
cp ~/.claude/CLAUDE.md "/Users/itocruz/Desktop/ObsidianVaults/Rafa's Brain/Claude Setup/Settings/CLAUDE-global.md"
cp ~/.claude/settings.json "/Users/itocruz/Desktop/ObsidianVaults/Rafa's Brain/Claude Setup/Settings/settings.json"
```

Then commit and push as usual.

**To restore on a new machine:** Clone this repo → copy `Claude Setup/Skills/` → `Claude Setup/CARL Domains/` → `Claude Setup/Settings/` into `~/.claude/`.

## Linking Rules

- Always use `[[double bracket]]` wikilinks to connect related notes.
- Every project note must link to relevant Knowledge notes and vice versa.
- Never create an isolated note.

## Git Commit Style

Use short, descriptive messages:
- `add: note on binary search`
- `update: EuroSide project decisions`
- `create: session summary 2026-03-23`
- `sync: skills after installing frontend-design`
