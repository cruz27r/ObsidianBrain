---
tags: [dashboard]
---

# Brain

> [!tip] Active Projects
> ```dataview
> TABLE status, priority, file.mtime AS "Updated"
> FROM "Dev/Projects" OR "Business" OR "Gaming"
> WHERE status = "active"
> SORT file.mtime DESC
> ```

> [!todo] Open Tasks
> ```tasks
> not done
> path does not include Templates
> path does not include Archive
> group by path
> limit 15
> ```

> [!warning] Inbox — Needs Processing
> ```dataview
> LIST
> FROM "00-Inbox"
> SORT file.ctime DESC
> ```

> [!note] Recent Notes
> ```dataview
> TABLE file.folder AS "Location", file.mtime AS "Modified"
> WHERE file.mtime >= date(today) - dur(7 days)
> AND file.folder != "Templates"
> AND file.name != "Home"
> SORT file.mtime DESC
> LIMIT 8
> ```

> [!abstract] Top Knowledge
> ```dataview
> TABLE length(file.inlinks) AS "Links In"
> FROM "Knowledge"
> SORT length(file.inlinks) DESC
> LIMIT 8
> ```
