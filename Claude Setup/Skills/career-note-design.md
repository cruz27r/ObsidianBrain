---
name: career-note-design
description: "Design and structure Career vault notes — interview prep tracker, job applications, resume notes. Applies progress callouts, difficulty badges, and correct structure for the Career domain."
---

# Career Note Design

Use this skill when creating or editing any note in `Career/`.

## CSS Dependency
Requires `career-styles.css` snippet enabled in Obsidian (Settings > Appearance > CSS Snippets).

## Interview Prep Tracker Structure

The main tracker note (`Career/Interview Prep Tracker.md`) uses this layout:

```markdown
---
tags: [career, interview-prep]
status: active
created: YYYY-MM-DD
---

# Interview Prep Tracker

> [!progress] Algorithm Progress
> ```dataview
> TABLE status, file.mtime AS "Last Reviewed"
> FROM "Knowledge/Algorithms"
> SORT status ASC, file.mtime ASC
> ```

> [!progress] Data Structure Progress
> ```dataview
> TABLE status, file.mtime AS "Last Reviewed"
> FROM "Knowledge/Data Structures"
> SORT status ASC, file.mtime ASC
> ```

> [!note] Problem Log
> | Date | Problem | Pattern | Difficulty | Result |
> |------|---------|---------|------------|--------|

> [!tip] Company Tracker
> | Company | Role | Status | Applied | Notes |
> |---------|------|--------|---------|-------|

> [!todo] Study Plan
> - [ ] item

> [!warning] Weak Areas
> Patterns I keep missing.
```

## Callout Reference

| Callout | Purpose | Color |
|---------|---------|-------|
| `[!progress]` | Wraps Dataview progress tables | Teal |
| `[!easy]` | Difficulty badge — title only | Green |
| `[!medium]` | Difficulty badge — title only | Amber |
| `[!hard]` | Difficulty badge — title only | Red |
| `[!note]` | Problem log table | Purple (from clean-polish) |
| `[!tip]` | Company tracker | Green (from clean-polish) |
| `[!todo]` | Study plan checklist | Blue (from clean-polish) |
| `[!warning]` | Weak areas / blockers | Orange (from clean-polish) |

## Tag Conventions for Problem Log

In the Pattern column of the problem log, use inline tags for color coding:
- `#binary-search`, `#two-pointers`, `#sliding-window`, `#bfs`, `#dfs`, `#fast-slow` → purple
- `#dp`, `#backtracking`, `#greedy` → orange

In the Status column of Company Tracker:
- `#applied` → blue
- `#interviewing` → amber
- `#rejected` → red (muted)
- `#offer` → green

## Routing
- Interview prep tracker → `Career/Interview Prep Tracker.md`
- Job application notes → `Career/Applications/<company>.md`
- Resume versions → `Career/Resume/`
- Behavioral prep → `Career/Behavioral/`

## Linking Rules
- Interview Prep Tracker links to `[[Algorithm Decision Tree]]`
- Problem log entries link to the relevant algorithm note (e.g. `[[Binary Search]]`)
- Company notes link to relevant project work that can be referenced in interviews

## After Creating/Editing
Commit with: `update: interview prep tracker` or `add: career note`
Push to main.
