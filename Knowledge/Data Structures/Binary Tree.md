---
tags: [concept, data-structure, tree]
created: 2026-03-21
related: [BST, Heap (Priority Queue), Tree Traversals, DFS (Depth-First Search), BFS (Breadth-First Search)]
---

# Binary Tree

## What it is
A tree where each node has **at most two children** (left and right). No ordering requirement — that's a BST.

## Key vocabulary
| Term | Meaning |
|---|---|
| Root | Top node, no parent |
| Leaf | Node with no children |
| Height | Longest path from root to a leaf |
| Depth of node | Distance from root to that node |
| Balanced | Height of left and right subtrees differ by at most 1 at every node |
| Complete | All levels filled except possibly last, which fills left to right |
| Full | Every node has 0 or 2 children (never 1) |
| Perfect | All internal nodes have 2 children, all leaves at same depth |

**Balanced tree height** = O(log n). **Skewed tree** (like a linked list) = O(n).

## Diagram — Tree Structure

```mermaid
graph TD
    classDef root fill:#1e3a5f,stroke:none,color:#fff,font-weight:bold
    classDef internal fill:#1d4ed8,stroke:none,color:#fff
    classDef leaf fill:#dbeafe,stroke:#1d4ed8,color:#1e3a5f
    A((1)):::root --> B((2)):::internal & C((3)):::internal
    B --> D((4)):::leaf & E((5)):::leaf
    C --> F((6)):::leaf & G((7)):::leaf
```

*Root (navy) → internal nodes (blue) → leaves (light, no children)*

## How Levels Work — Why It Matters

```mermaid
flowchart LR
    classDef l0 fill:#1e3a5f,stroke:none,color:#fff
    classDef l1 fill:#1d4ed8,stroke:none,color:#fff
    classDef l2 fill:#dbeafe,stroke:#1d4ed8,color:#1e3a5f
    subgraph "Level 0 — 1 node"
        A((root)):::l0
    end
    subgraph "Level 1 — 2 nodes"
        B((L)):::l1
        C((R)):::l1
    end
    subgraph "Level 2 — 4 nodes"
        D((LL)):::l2
        E((LR)):::l2
        F((RL)):::l2
        G((RR)):::l2
    end
    A --> B & C
    B --> D & E
    C --> F & G
```

*Each level doubles. n nodes = log₂(n) levels. 1 million nodes → only ~20 levels deep.*

## Balanced vs Unbalanced — The Critical Difference

```mermaid
flowchart TD
    classDef good fill:#166534,stroke:none,color:#fff
    classDef bad fill:#991b1b,stroke:none,color:#fff
    subgraph balanced["Balanced — height = log n  →  O(log n) operations"]
        A1((1)):::good --> B1((2)) & C1((3))
        B1 --> D1((4)) & E1((5))
        C1 --> F1((6)) & G1((7))
    end
    subgraph skewed["Skewed — height = n  →  O(n) operations"]
        A2((1)):::bad --> B2((2)) --> C2((3)) --> D2((4)) --> E2((5))
    end
```

*Skewed = effectively a linked list. Self-balancing trees (AVL, Red-Black) prevent this.*

## The Recursive Decision Pattern

```mermaid
flowchart TD
    classDef start fill:#1e3a5f,stroke:none,color:#fff
    classDef step fill:#1d4ed8,stroke:none,color:#fff
    classDef base fill:#374151,stroke:none,color:#f9fafb
    Q(["At each node"]):::start --> B["Ask left subtree"]:::step & C["Ask right subtree"]:::step
    B & C --> D["Combine: left + right + node.val"]:::step
    D --> E["Return answer to parent"]:::step
    E --> F(["Base case: null → return 0"]):::base
```

**Examples of this pattern:**
- Max depth → `1 + max(leftDepth, rightDepth)`
- Sum of all nodes → `left + right + node.val`
- Is balanced? → `abs(leftHeight - rightHeight) <= 1`

## TypeScript node definition
```typescript
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}
```

## The 4 traversals (brief)
Full implementations in [[Tree Traversals]].
- **Inorder** (left → root → right): for BST, gives sorted order
- **Preorder** (root → left → right): serialization, copying
- **Postorder** (left → right → root): deletion, subtree calculations
- **Level-order** (BFS): process by depth, shortest path

## Common recursive patterns

### Max depth — O(n)
```typescript
function maxDepth(root: TreeNode | null): number {
  if (!root) return 0;
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
```

### Check if balanced — O(n)
```typescript
function isBalanced(root: TreeNode | null): boolean {
  function height(node: TreeNode | null): number {
    if (!node) return 0;
    const left = height(node.left);
    if (left === -1) return -1; // early exit
    const right = height(node.right);
    if (right === -1) return -1;
    if (Math.abs(left - right) > 1) return -1; // unbalanced signal
    return 1 + Math.max(left, right);
  }
  return height(root) !== -1;
}
```

### Lowest Common Ancestor — O(n)
```typescript
function lowestCommonAncestor(root: TreeNode | null, p: TreeNode, q: TreeNode): TreeNode | null {
  if (!root || root === p || root === q) return root;
  const left = lowestCommonAncestor(root.left, p, q);
  const right = lowestCommonAncestor(root.right, p, q);
  // If found in both subtrees, current node is LCA
  if (left && right) return root;
  return left ?? right;
}
```

### Recursion mental model
Most tree problems follow: **"What do I need from my children to answer the question for the current node?"**
- Max depth: max of children + 1
- Sum: sum of children + my value
- Is symmetric: are left and right subtrees mirrors?

## Multi-Language Reference — Max Depth of Binary Tree

```javascript
// JavaScript
function maxDepth(root) {
  if (!root) return 0;
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
```

```java
// Java
public int maxDepth(TreeNode root) {
    if (root == null) return 0;
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
```

```python
# Python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

```c
// C
int maxDepth(struct TreeNode* root) {
    if (!root) return 0;
    int left = maxDepth(root->left);
    int right = maxDepth(root->right);
    return 1 + (left > right ? left : right);
}
```

```cpp
// C++
int maxDepth(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}
```

## Practice & Resources

**LeetCode — Essential Problems**
- [104 · Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) — Easy · simplest recursive pattern
- [226 · Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) — Easy · swap children recursively
- [543 · Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) — Easy · combine left + right height
- [102 · Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) — Medium · BFS on tree
- [105 · Construct Binary Tree from Preorder and Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) — Medium · rebuild from traversals
- [124 · Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) — Hard · gain vs contribution distinction

**References**
- [VisuAlgo · Binary Tree](https://visualgo.net/en/bst) — animated insert/search/delete
- [NeetCode · Trees playlist](https://neetcode.io/roadmap)

## Related
- [[BST]] — binary tree with ordering property
- [[Tree Traversals]] — inorder, preorder, postorder, level-order
- [[DFS (Depth-First Search)]] — all non-level-order traversals are DFS
- [[BFS (Breadth-First Search)]] — level-order traversal
