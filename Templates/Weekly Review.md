---
tags: [weekly-review]
week: <% tp.date.now("YYYY-[W]WW") %>
created: <% tp.date.now("YYYY-MM-DD") %>
---

# Week of <% tp.date.now("MMMM D, YYYY") %>

> [!tip] What got done
> -

> [!warning] What didn't get done (and why)
> -

> [!abstract] Inbox — still unprocessed?
> ```dataview
> LIST FROM "00-Inbox" SORT file.ctime ASC
> ```

> [!abstract] Active Projects — any blockers?
> ```dataview
> TABLE status FROM "Dev/Projects" OR "Business" WHERE status = "active"
> ```

> [!todo] Next week priorities
> 1.
> 2.
> 3.

---
[[Home]]
