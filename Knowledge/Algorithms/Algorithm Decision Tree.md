---
tags: [concept, algorithm, reference, cheatsheet]
created: 2026-03-21
related: [BFS (Breadth-First Search), DFS (Depth-First Search), Dynamic Programming, Two Pointers, Sliding Window, Binary Search, Backtracking, Greedy, Union-Find (Disjoint Set)]
---

> [!pattern] Meta · Navigation

# Algorithm Decision Tree

Use this when you see a problem and don't know where to start. Follow the questions.

## Step 1 — What kind of data?

```mermaid
flowchart TD
    classDef start fill:#1e3a5f,stroke:none,color:#fff
    classDef answer fill:#1d4ed8,stroke:none,color:#fff
    classDef route fill:#374151,stroke:none,color:#f9fafb
    START(["You have a problem"]):::start --> A{What is the input?}
    A -->|Array or string| B{Is it sorted?}
    A -->|Tree| TREE["→ Step 2"]:::route
    A -->|Graph or grid| GRAPH["→ Step 3"]:::route
    A -->|Find min / max / count| OPT["→ Step 4"]:::route
    B -->|Yes| C{Find a target?}
    B -->|No| D{Window / subarray?}
    C -->|Yes| BS["Binary Search  ·  O(log n)"]:::answer
    C -->|No| TP["Two Pointers  ·  O(n)"]:::answer
    D -->|Fixed size| SW["Sliding Window  ·  fixed"]:::answer
    D -->|Variable size| SW2["Sliding Window  ·  variable"]:::answer
    D -->|Pairs or triplets| TP2["Two Pointers"]:::answer
    D -->|Range sums| PS["Prefix Sum"]:::answer
```

## Step 2 — Tree problems

```mermaid
flowchart TD
    classDef start fill:#1e3a5f,stroke:none,color:#fff
    classDef answer fill:#1d4ed8,stroke:none,color:#fff
    classDef special fill:#6d28d9,stroke:none,color:#fff
    TREE(["Tree input"]):::start --> A{Level order or depth?}
    A -->|Level-order / shortest path| BFS["BFS  ·  queue"]:::answer
    A -->|By depth / structure| B{Recursive natural?}
    B -->|Yes| DFS["DFS recursive"]:::answer
    B -->|Need explicit stack| DFSI["DFS iterative"]:::answer
    DFS --> C{Track choices / path?}
    C -->|Yes — try all paths| BT["Backtracking  ·  DFS + undo"]:::special
    C -->|No — just traverse| DFS
```

## Step 3 — Graph problems

```mermaid
flowchart TD
    classDef start fill:#1e3a5f,stroke:none,color:#fff
    classDef answer fill:#1d4ed8,stroke:none,color:#fff
    classDef alt fill:#374151,stroke:none,color:#f9fafb
    GRAPH(["Graph or grid input"]):::start --> A{Need shortest path?}
    A -->|Yes, unweighted| BFS["BFS  ·  guarantees fewest hops"]:::answer
    A -->|Yes, weighted| DIJ["Dijkstra  ·  min-heap + BFS"]:::answer
    A -->|No| B{Connectivity queries?}
    B -->|Static — one time check| DFS["DFS flood fill"]:::answer
    B -->|Dynamic — edges added over time| UF["Union-Find  ·  near O(1) per query"]:::answer
    B --> C{Cycle / ordering?}
    C -->|Cycle detection| DFS2["DFS  ·  color marking"]:::answer
    C -->|Topological sort| TOPO["Kahn's BFS  ·  or DFS finish-time"]:::alt
```

## Step 4 — Optimization problems

```mermaid
flowchart TD
    classDef start fill:#1e3a5f,stroke:none,color:#fff
    classDef answer fill:#1d4ed8,stroke:none,color:#fff
    classDef key fill:#166534,stroke:none,color:#fff
    classDef alt fill:#374151,stroke:none,color:#f9fafb
    OPT(["Find min / max / count ways"]):::start --> A{Greedy works?}
    A -->|Yes — local best = global best| GR["Greedy  ·  O(n) or O(n log n)"]:::answer
    A -->|No — must consider all options| B{Overlapping subproblems?}
    B -->|Yes — same state recomputed| DP["Dynamic Programming"]:::key
    B -->|No — subproblems independent| DC["Divide & Conquer"]:::alt
    DP --> C{State dimensions?}
    C -->|1D  ·  dp[i]| DP1["Fibonacci · coin change · stairs"]:::answer
    C -->|2D  ·  dp[i][j]| DP2["Grid paths · LCS · knapsack"]:::answer
```

---

## Quick Reference — Pattern Triggers

| You see this in the problem... | Reach for... |
|---|---|
| "sorted array", "find target" | [[Binary Search]] |
| "subarray with sum/length condition" | [[Sliding Window]] |
| "two elements that sum to X" | [[Two Pointers]] |
| "minimum steps / shortest path" | [[BFS (Breadth-First Search)]] |
| "all possible combinations / paths" | [[Backtracking]] |
| "max/min of overlapping subproblems" | [[Dynamic Programming]] |
| "can always take the locally best" | [[Greedy]] |
| "connected components / same group" | [[Union-Find (Disjoint Set)]] |
| "detect cycle in graph" | [[DFS (Depth-First Search)]] |
| "prefix matching / autocomplete" | [[Trie]] |
| "kth largest / top k elements" | [[Heap (Priority Queue)]] |

---

## Related
- [[BFS (Breadth-First Search)]]
- [[DFS (Depth-First Search)]]
- [[Dynamic Programming]]
- [[Two Pointers]]
- [[Sliding Window]]
- [[Binary Search]]
- [[Backtracking]]
- [[Greedy]]
- [[Union-Find (Disjoint Set)]]
