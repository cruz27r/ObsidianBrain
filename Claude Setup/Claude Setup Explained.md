# Claude Setup — How It Works & Why

## What Is This Folder?

`Claude Setup/` is a backup and reference for how Claude Code is configured on your machine. It mirrors the files inside `~/.claude/` so you can restore everything on a new machine, understand your setup at a glance, and track changes over time via git.

---

## The Architecture

### Before (one big file)
Everything lived in a single `CLAUDE.md` — workflow rules, skill routing, working rules, multi-agent instructions, all piled together. It was long, hard to update, and Claude had to load all of it every session even when most of it wasn't relevant.

### After (modular `@includes`)
`CLAUDE.md` is now lean — just 15 lines. It delegates to 6 focused files:

| File | What it covers |
|------|---------------|
| `instructions/workflow.md` | Session start, planning, TDD, review cycle, debugging, branch completion |
| `instructions/skill-routing.md` | Which skill/MCP to reach for per task type |
| `instructions/carl-domains.md` | Keyword-triggered auto-injection (Shopify, Gaming, Notes, etc.) |
| `instructions/context-efficiency.md` | Stay concise, no noise, summarize don't dump |
| `instructions/working-rules.md` | Minimal changes, security, visual verification, caching caveats |
| `instructions/multi-agent.md` | Parallel agents, worktree isolation, subagent prompt template |

Each file has exactly one job. When you need to update a rule you go to one file, not hunt through 200 lines.

---

## Why It's Better

**1. Easier to maintain**
Edit one focused file instead of scrolling through a monolith.

**2. Faster sessions**
Claude reads what it needs. Shorter CLAUDE.md = less token overhead at session start.

**3. Clear mental model**
You can glance at `CLAUDE.md` and immediately know the shape of the whole system without reading all the rules.

**4. Safer updates**
You can change `working-rules.md` without accidentally breaking the workflow or skill-routing sections.

**5. Survives machine resets**
Everything in `~/.claude/` is backed up here. Clone this vault on a new machine → copy the files back → you're fully restored.

---

## Skills

`Claude Setup/Skills/` contains the installed skill prompts. These are loaded by Claude Code's Superpowers system. Each skill is a named prompt that expands into a full workflow when invoked (e.g. `brainstorming`, `systematic-debugging`, `using-git-worktrees`).

Skills > memory for workflows because they're structured, versioned, and repeatable — not fuzzy recollections.

---

## How to Restore on a New Machine

```bash
git clone https://github.com/cruz27r/ObsidianBrain
cp -r "Claude Setup/Settings/CLAUDE-global.md" ~/.claude/CLAUDE.md
cp -r "Claude Setup/Settings/settings.json" ~/.claude/settings.json
# Then reinstall skills via Claude Code Superpowers
```

---

## Related Notes
- [[Dev/Projects/Claude Code Setup]]
- [[Knowledge/Tech Concepts/Obsidian vs NotebookLM]]
