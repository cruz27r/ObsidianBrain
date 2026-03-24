---
tags: [inbox, session-summary]
created: 2026-03-21
status: unprocessed
---

# Session Summary — 2026-03-21

## What we built today

### 1. Obsidian Vault Setup
- Created full PARA structure: 00-Inbox, 01-Projects, 02-Areas, 03-Resources, 04-Archive, Templates
- Templates: Project.md, Concept.md, Idea.md
- NOTES CARL domain set to always-on — auto-note behavior active every session

### 2. Project Notes Created
- [[01-Projects/EuroSide Website/EuroSide - Project Reference]] — full brand guidelines, colors, image map, components, pending go-live items
- [[01-Projects/Discord Bot/Discord Bot - Phase 1]] — all decisions locked, commands, folder structure, step-by-step setup guide

### 3. SWE Interview Reference Library — 24 notes

**Data Structures (10):** [[Arrays & Strings]], [[Linked List]], [[Stack]], [[Queue & Deque]], [[Binary Tree]], [[BST (Binary Search Tree)]], [[Heap (Priority Queue)]], [[Trie]], [[Graph]], [[Union-Find (Disjoint Set)]]

**Algorithms (14):** [[Big O Notation]], [[Binary Search]], [[Sorting Algorithms]], [[BFS (Breadth-First Search)]], [[DFS (Depth-First Search)]], [[Tree Traversals]], [[Two Pointers]], [[Sliding Window]], [[Fast & Slow Pointers]], [[Backtracking]], [[Dynamic Programming]], [[Greedy]], [[Divide & Conquer]], [[Bit Manipulation]]

**Tech Concepts:** [[Hash Tables]], [[REST vs GraphQL]]

**Indexes:** [[03-Resources/System Design/README]], [[03-Resources/Design Patterns/README]]

### 4. Cleanup
- Removed redundant `CodeMSC/euroside/` and `euroside_project.txt` — canonical repo is at `~/Desktop/EuroSide/`
- Discord bot scaffold at `~/Desktop/CodeMSC/discord-bot/` — TypeScript, npm installed, compiles clean

## Pending actions (yours)
- [ ] Install **Local REST API** plugin in Obsidian → copy key → paste in `~/.claude/mcp.json` → restart Claude Code
- [ ] Create Discord app at discord.dev → fill `.env` → run `npx ts-node deploy-commands.ts`
- [ ] Replace placeholder images in EuroSide before go-live
- [ ] Add real Gmail App Password + Stripe links to EuroSide

## Process established
Going forward: any new project → `01-Projects/` note. Any concept explained → `03-Resources/` note. All notes linked with `[[wikilinks]]`.
