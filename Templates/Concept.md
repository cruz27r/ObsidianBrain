<%* const name = await tp.system.prompt("Concept name") _%>
<%* const category = await tp.system.prompt("Category (algorithm/data-structure/tech-concept/design-pattern)") _%>
<%* const pattern = await tp.system.prompt("Pattern type (e.g. Searching · Divide & Conquer)") _%>
<%* await tp.file.rename(name) _%>
---
tags: [concept, <%= category %>]
created: <% tp.date.now("YYYY-MM-DD") %>
related: []
---

> [!pattern] <%= pattern %>

# <%= name %>

## What it is
Plain explanation anyone can understand.

> [!complexity] Complexity
> | | |
> |---|---|
> | Time | |
> | Space | |

> [!use] When to Use
> -
> -

> [!avoid] When NOT to Use
> -
> -

## How it works
Step-by-step explanation or diagram.

> [!example]- TypeScript
> ```typescript
>
> ```

> [!example]- JavaScript
> ```javascript
>
> ```

## Practice
- LeetCode:

## Related
- [[]]
