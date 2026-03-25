---
tags: [dashboard]
---

# Dashboard

## Active Projects
```dataview
TABLE status, priority, file.mtime AS "Last Updated"
FROM "Dev/Projects" OR "Business" OR "Gaming"
WHERE status = "active"
SORT file.mtime DESC
```

## Inbox — Needs Processing
```dataview
LIST
FROM "00-Inbox"
SORT file.ctime DESC
```

## Open Tasks
```tasks
not done
path does not include Templates
path does not include Archive
group by path
limit 20
```

## Recent Notes
```dataview
TABLE file.mtime AS "Modified"
WHERE file.mtime >= date(today) - dur(7 days)
AND file.folder != "Templates"
SORT file.mtime DESC
LIMIT 10
```

## Knowledge Areas
```dataview
TABLE length(file.inlinks) AS "Linked From", file.mtime AS "Last Updated"
FROM "Knowledge"
SORT length(file.inlinks) DESC
LIMIT 10
```
