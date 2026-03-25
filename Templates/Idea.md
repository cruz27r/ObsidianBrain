<%* const name = await tp.system.prompt("Idea name") _%>
<%* const category = await tp.system.prompt("Category (tech/business/gaming/career/other)") _%>
<%* await tp.file.rename(name) _%>
---
tags: [idea, <%= category %>]
created: <% tp.date.now("YYYY-MM-DD") %>
status: raw
related: []
---

# <%= name %>

## The idea
One paragraph — what is it, why does it matter.

## Why now
What triggered this? What problem does it solve?

## Open questions
- ?

## Next step
- [ ]

## Related
- [[]]
