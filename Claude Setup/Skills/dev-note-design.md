---
name: dev-note-design
description: "Design and structure Dev/Projects vault notes. Applies status banners, architecture callouts, phase tracking, and correct frontmatter for the Dev domain."
---

# Dev Note Design

Use this skill when creating or editing any note in `Dev/Projects/`.

## CSS Dependency
Requires `dev-styles.css` snippet enabled in Obsidian (Settings > Appearance > CSS Snippets).

## Required Structure

Every Dev project note follows this layout:

```markdown
---
tags: [project, <status>]
status: planning | active | paused | complete
created: YYYY-MM-DD
priority: high | medium | low
tech: [framework, language, tools]
linked: []
---

> [!status-<status>] Status — <Status> · <one-line context>

# Project Name

## Goal
One sentence: what does this build and why.

> [!arch] Architecture
> Key decisions, stack, folder structure.
> ```
> project/
> ├── src/
> └── ...
> ```

## Phases
- [ ] Phase 1 —
- [ ] Phase 2 —
- [ ] Phase 3 —

## Resources
- Spec: [[plan note or doc]]
- Repo: path or URL

## Notes
- YYYY-MM-DD: Running log of decisions and blockers.

## Related
- [[related knowledge note]]
- [[related project]]
```

## Callout Reference

| Callout | Purpose | Color |
|---------|---------|-------|
| `[!status-planning]` | Planning status banner — title only | Blue |
| `[!status-active]` | Active status banner — title only | Green |
| `[!status-paused]` | Paused status banner — title only | Amber |
| `[!status-complete]` | Complete status banner — title only | Muted green |
| `[!arch]` | Architecture section (diagrams, folder trees) | Blue |
| `[!todo]` | Open tasks or pending phases | Blue (from clean-polish) |

## Status Banner Usage
The status banner is always the first thing after the frontmatter. It reads:
`> [!status-<status>] Status — <Status> · <short context>`

Example: `> [!status-active] Status — Active · Pending Real Photos`

Update the banner when status changes. The `status` frontmatter field and banner must stay in sync.

## Dev Log Notes
For dev log / session notes in the same project folder:
- Use `> [!todo]` to wrap the Tasks plugin query
- Add a new dated session entry at the top (most recent first)
- Log architecture decisions in the decisions table

## Routing
- All dev project notes → `Dev/Projects/<project-name>/`
- Dev logs → `Dev/Projects/<project-name>/Dev Log.md`
- Setup/architecture guides → `Dev/Projects/<project-name>/`

## Linking Rules
- Every project links to relevant `Knowledge/` notes
- Dev logs link back to the main project spec note
- Architecture notes link to `Knowledge/Tech Concepts/` for patterns used

## After Creating/Editing
Commit with: `add: <note name>` or `update: <project name>`
Push to main.
