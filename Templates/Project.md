<%* const name = await tp.system.prompt("Project name") _%>
<%* const status = await tp.system.prompt("Status (planning/active/paused/complete)") _%>
<%* const priority = await tp.system.prompt("Priority (high/medium/low)") _%>
<%* const tech = await tp.system.prompt("Tech stack (comma separated)") _%>
<%* await tp.file.rename(name) _%>
---
tags: [project, <%= status %>]
status: <%= status %>
created: <% tp.date.now("YYYY-MM-DD") %>
priority: <%= priority %>
tech: [<%= tech %>]
linked: []
---

> [!status-<%= status %>] Status — <%= status %>

# <%= name %>

## Goal
One sentence: what does this build and why.

> [!arch] Architecture
> Key decisions, stack, folder structure.

## Phases
- [ ] Phase 1 —
- [ ] Phase 2 —
- [ ] Phase 3 —

## Resources
- Spec: [[]]
- Repo:

## Notes
- <% tp.date.now("YYYY-MM-DD") %>: Project created.

## Related
- [[]]
