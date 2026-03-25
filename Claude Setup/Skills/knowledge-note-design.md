---
name: knowledge-note-design
description: "Design and structure Knowledge vault notes (algorithms, data structures, tech concepts). Applies the correct callout blocks, CSS snippet, frontmatter, and wikilinks for the Knowledge domain."
---

# Knowledge Note Design

Use this skill when creating or editing any note in `Knowledge/Algorithms/`, `Knowledge/Data Structures/`, or `Knowledge/Tech Concepts/`.

## CSS Dependency
Requires `knowledge-styles.css` snippet enabled in Obsidian (Settings > Appearance > CSS Snippets).

## Required Structure

Every Knowledge note must follow this exact layout:

```markdown
---
tags: [concept, <category>]
created: YYYY-MM-DD
related: []
---

> [!pattern] <Pattern Type> · <Category>

# Note Title

## What it is
Plain explanation anyone can understand.

> [!complexity] Complexity
> | | |
> |---|---|
> | Time | O(...) |
> | Space | O(...) |

> [!use] When to Use
> - condition 1
> - condition 2

> [!avoid] When NOT to Use
> - condition 1
> - condition 2

## How it works
Step-by-step explanation or diagram (Mermaid if helpful).

> [!example]- TypeScript
> ```typescript
> // code here
> ```

> [!example]- JavaScript
> ```javascript
> // code here
> ```

## Practice
- LeetCode: problem name + link

## Related
- [[related note]]
- [[related note]]
```

## Callout Reference

| Callout | Purpose | Color |
|---------|---------|-------|
| `[!pattern]` | Pattern-type badge at top — title only | Purple |
| `[!complexity]` | Time/space table — monospace teal | Teal |
| `[!use]` | When to use this pattern | Green |
| `[!avoid]` | When NOT to use | Red-orange |
| `[!example]-` | Code per language — collapsed by default (the `-` is required) | Purple |

## Pattern Labels by Category

**Algorithms:**
- Binary Search → `Searching · Divide & Conquer`
- BFS → `Graph Traversal · Level-Order`
- DFS → `Graph Traversal · Recursion · Stack`
- DP → `Optimization · Memoization · Tabulation`
- Backtracking → `Recursion · State Space Search`
- Greedy → `Optimization · Local Choices`
- Sliding Window → `Array · Two-Pointer Variant`
- Two Pointers → `Array · Linear Scan`
- Fast & Slow Pointers → `Linked List · Cycle Detection`

**Data Structures:**
- Graph → `Adjacency · Traversal · Connectivity`
- Binary Tree → `Hierarchical · Recursion`
- BST → `Hierarchical · Searching · Sorting`
- Heap → `Ordering · Top-K · Priority`
- Linked List → `Sequential · Pointer Manipulation`
- Stack → `LIFO · Monotonic`
- Queue → `FIFO · Sliding Window`
- Trie → `String · Prefix Tree`
- Union-Find → `Connectivity · Grouping`

## Routing
- Algorithms → `Knowledge/Algorithms/`
- Data Structures → `Knowledge/Data Structures/`
- Tech concepts (REST, GraphQL, etc.) → `Knowledge/Tech Concepts/`
- Design patterns → `Knowledge/Design Patterns/`
- System design → `Knowledge/System Design/`

## Linking Rules
- Every note links to at least one related note via `[[wikilink]]`
- Algorithm notes link to relevant data structure notes and vice versa
- Tech concept notes link to projects that use them
- `Algorithm Decision Tree` links to every algorithm note

## After Creating/Editing
Commit with: `add: <note name>` or `update: <note name>`
Push to main.
