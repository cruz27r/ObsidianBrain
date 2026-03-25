---
tags: [weekly-review]
week: <% tp.date.now("YYYY-[W]WW") %>
created: <% tp.date.now("YYYY-MM-DD") %>
---

# Week of <% tp.date.now("MMMM D, YYYY") %>

## What got done
-

## What didn't get done (and why)
-

## Inbox processed?
```dataview
LIST FROM "00-Inbox" SORT file.ctime ASC
```

## Active projects — any blockers?
```dataview
TABLE status FROM "Dev/Projects" OR "Business" WHERE status = "active"
```

## Next week priorities
1.
2.
3.

## Links
- [[Home]]
