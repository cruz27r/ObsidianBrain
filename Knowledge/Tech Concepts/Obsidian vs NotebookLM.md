# Obsidian vs NotebookLM — Planning & Workflow Comparison

**Date:** 2026-03-24
**Context:** Evaluating current Obsidian setup against NotebookLM for personal knowledge + project work

---

## What You Have in Obsidian Right Now

| Area | Current State |
|------|--------------|
| Algorithm reference | 14 structured notes (BFS, DP, Backtracking, etc.) |
| Data structures | 10 notes (Trees, Graphs, Heaps, etc.) |
| Tech concepts | Growing (`[[Hash Tables]]`, `[[REST vs GraphQL]]`) |
| Active projects | `[[Discord Bot - Phase 1]]`, `[[EuroSide - Project Reference]]` |
| Claude skills | 15 documented skills in `Claude Setup/Skills/` |
| Linking | Wikilinks wired across 23+ notes |
| Plugins | Smart Connections, Omnisearch, Excalidraw |
| Workflow | Git-integrated, auto-push on every change |

---

## Core Difference in Philosophy

| | **Obsidian** | **NotebookLM** |
|---|---|---|
| **Model** | You build the knowledge | You feed it sources, it synthesizes |
| **Persistence** | Everything lives locally, versioned | Cloud-only, session/notebook-scoped |
| **Control** | 100% yours — structure, links, format | Guided by Google's AI, limited structure control |
| **AI role** | Claude via MCP + Smart Connections | Built-in Gemini, tightly integrated |
| **Output** | Notes, plans, project docs | Summaries, Q&A, audio overviews, briefings |
| **Linking** | Manual wikilinks + Smart Connections | Automatic citation back to source |

---

## Where Obsidian Wins (For You)

### 1. Long-term personal knowledge base
Your algorithm + data structure notes are reference material you'll use for years. Obsidian owns this category — notes persist, evolve, and link to your projects.

### 2. Project command center
`Dev/Projects/`, `Business/`, `Career/` — your vault is already a living project tracker. NotebookLM can't track phases, statuses, or decisions across time.

### 3. Claude integration depth
Your 15-skill setup + CARL domains + MCP routing means Claude can read, write, and navigate your vault natively. That's a custom AI brain — NotebookLM can't match this depth of personalization.

### 4. Offline + git-versioned
Everything is local and in git. You can roll back, branch, and own your data completely.

### 5. Linking between ideas
`[[wikilinks]]` and Smart Connections surface unexpected connections across notes. This compounds over time as your vault grows.

---

## Where NotebookLM Wins

### 1. Processing external documents fast
Drop in a PDF paper, a book chapter, a YouTube transcript, a research doc — NotebookLM immediately lets you query it, summarize it, ask questions about it. Obsidian requires you to manually distill the content first.

### 2. Source-cited answers
Every answer cites exactly which source it came from. Useful for research, school, or when accuracy matters and you need to trace claims.

### 3. Audio overviews ("podcast" mode)
NotebookLM can generate a conversational audio overview of your sources. Great for reviewing dense material while commuting or away from a screen.

### 4. Zero-setup synthesis
No structure needed upfront. Upload 10 documents and immediately start chatting. Obsidian requires curation.

### 5. School / research workflows
If you're reading papers, textbooks, or lecture slides, NotebookLM is significantly faster at digesting and explaining that material than building Obsidian notes manually.

---

## Honest Weaknesses

### Obsidian weaknesses
- High maintenance: you have to write the notes, maintain links, keep it updated
- Cold start: a new area of your vault is empty until you build it
- Processing dense external sources is manual work
- Smart Connections is good but not as conversational as NotebookLM

### NotebookLM weaknesses
- Not a long-term memory system — notebooks are isolated buckets
- No persistent linking between notebooks or ideas over time
- Google controls your data; no git, no versioning
- You can't build custom AI workflows on top of it (no skills, no hooks)
- No project tracking, no status updates, no structured notes
- Loses context outside a specific notebook

---

## Decision Framework: Which To Use

| Situation | Use |
|-----------|-----|
| Studying an algorithm for an interview | **Obsidian** — build the note, link it, own it |
| Reading a research paper or textbook chapter | **NotebookLM** — upload + query instantly |
| Tracking project phases and decisions | **Obsidian** — persistent project doc |
| School — reviewing lecture slides before an exam | **NotebookLM** — fast synthesis |
| Building your career/interview prep | **Obsidian** — long-term resource |
| One-off research task (compare 5 articles) | **NotebookLM** — disposable synthesis |
| Claude skills, workflows, MCP config | **Obsidian** — lives here, full control |
| Generating audio review of a dense book | **NotebookLM** — unique capability |

---

## Recommended Hybrid Approach

Use both — they solve different problems.

```
External Sources (PDFs, papers, lectures)
        ↓
   NotebookLM  ←── quick synthesis, Q&A, audio review
        ↓
  Key insights distilled
        ↓
   Obsidian  ←── permanent note, linked into Knowledge/
        ↓
   Claude (MCP) ←── builds on your notes, updates projects
```

**Practical flow:**
1. Encounter a dense source (paper, book, lecture) → load into NotebookLM first
2. Extract the key insights / answers you need
3. Write a concise Obsidian note with those insights in the right folder
4. Wire it into your existing knowledge graph with wikilinks
5. That note becomes a permanent asset Claude can reference

---

## What's Missing From Your Vault Right Now

Based on what you have, these areas would benefit from expansion:

- `School/` — empty; if you're taking courses, NotebookLM + Obsidian hybrid here is powerful
- `Career/` — empty; interview prep notes should live here (`[[Algorithm Decision Tree]]` links here)
- `Knowledge/System Design/` — stub only; a real system design section would pair well with your algo notes
- `Knowledge/Design Patterns/` — stub only; should link to your Discord Bot and EuroSide projects

---

## Related Notes

- [[Algorithm Decision Tree]]
- [[Hash Tables]]
- [[REST vs GraphQL]]
- [[Discord Bot - Phase 1]]
- [[EuroSide - Project Reference]]
