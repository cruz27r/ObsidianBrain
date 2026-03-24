---
tags: [concept, algorithm, tree]
created: 2026-03-21
related: [Binary Tree, BST (Binary Search Tree), DFS (Depth-First Search), BFS (Breadth-First Search), Stack]
---

# Tree Traversals

## The 4 traversals at a glance

| Traversal | Order | Key use case |
|---|---|---|
| **Inorder** | left → root → right | [[BST (Binary Search Tree)|BST]] sorted output, kth smallest |
| **Preorder** | root → left → right | Serialize/copy tree, path problems |
| **Postorder** | left → right → root | Delete tree, subtree aggregation |
| **Level-order** | [[BFS (Breadth-First Search)|BFS]] by depth | Min depth, right side view, zigzag |

## Recursive implementations (simple, clean)

```typescript
// Inorder — L, Root, R
function inorder(root: TreeNode | null, result: number[] = []): number[] {
  if (!root) return result;
  inorder(root.left, result);
  result.push(root.val);
  inorder(root.right, result);
  return result;
}

// Preorder — Root, L, R
function preorder(root: TreeNode | null, result: number[] = []): number[] {
  if (!root) return result;
  result.push(root.val);
  preorder(root.left, result);
  preorder(root.right, result);
  return result;
}

// Postorder — L, R, Root
function postorder(root: TreeNode | null, result: number[] = []): number[] {
  if (!root) return result;
  postorder(root.left, result);
  postorder(root.right, result);
  result.push(root.val);
  return result;
}
```

## Iterative implementations (interviewers love asking for these)

### Iterative inorder — using a [[Stack|stack]]
```typescript
function inorderIterative(root: TreeNode | null): number[] {
  const result: number[] = [];
  const stack: TreeNode[] = [];
  let curr: TreeNode | null = root;

  while (curr || stack.length) {
    // Go as far left as possible
    while (curr) { stack.push(curr); curr = curr.left; }
    // Process
    curr = stack.pop()!;
    result.push(curr.val);
    // Move to right subtree
    curr = curr.right;
  }
  return result;
}
```

### Iterative preorder
```typescript
function preorderIterative(root: TreeNode | null): number[] {
  if (!root) return [];
  const result: number[] = [];
  const stack: TreeNode[] = [root];

  while (stack.length) {
    const node = stack.pop()!;
    result.push(node.val);
    // Push right first so left is processed first (LIFO)
    if (node.right) stack.push(node.right);
    if (node.left) stack.push(node.left);
  }
  return result;
}
```

### Iterative postorder (reverse of modified preorder)
```typescript
function postorderIterative(root: TreeNode | null): number[] {
  if (!root) return [];
  const result: number[] = [];
  const stack: TreeNode[] = [root];

  while (stack.length) {
    const node = stack.pop()!;
    result.unshift(node.val); // prepend — builds postorder in reverse
    if (node.left) stack.push(node.left);
    if (node.right) stack.push(node.right);
  }
  return result;
}
```

## Level-order (BFS) — returns array of arrays by level
```typescript
function levelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];
  const result: number[][] = [];
  const queue: TreeNode[] = [root];

  while (queue.length) {
    const levelSize = queue.length;
    const level: number[] = [];
    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift()!;
      level.push(node.val);
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    result.push(level);
  }
  return result;
}
```

## Problems that reveal which traversal to use

| Problem | Traversal | Why |
|---|---|---|
| Validate BST | Inorder | Should be strictly increasing |
| Kth smallest in BST | Inorder | BST sorted output |
| Serialize/deserialize tree | Preorder | Root first enables reconstruction |
| Path sum (root to leaf) | Preorder | Need parent value before children |
| Delete tree nodes | Postorder | Process children before parent |
| Evaluate expression tree | Postorder | Need child values before computing |
| Right side view | Level-order | Last node per level |
| Minimum depth | Level-order (BFS) | First leaf encountered = min depth |
| Zigzag level order | Level-order | Alternate direction per level |

## Multi-Language Reference — Inorder Traversal

```javascript
// JavaScript
function inorder(root, result = []) {
  if (!root) return result;
  inorder(root.left, result);
  result.push(root.val);
  inorder(root.right, result);
  return result;
}
```

```java
// Java
public static void inorder(TreeNode root, List<Integer> result) {
    if (root == null) return;
    inorder(root.left, result);
    result.add(root.val);
    inorder(root.right, result);
}
```

```python
# Python
def inorder(root, result=None):
    if result is None: result = []
    if not root: return result
    inorder(root.left, result)
    result.append(root.val)
    inorder(root.right, result)
    return result
```

```c
// C
void inorder(struct TreeNode* root) {
    if (!root) return;
    inorder(root->left);
    printf("%d ", root->val);
    inorder(root->right);
}
```

```cpp
// C++
void inorder(TreeNode* root, vector<int>& result) {
    if (!root) return;
    inorder(root->left, result);
    result.push_back(root->val);
    inorder(root->right, result);
}
```

## Practice & Resources

**LeetCode — Essential Problems**
- [94 · Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) — Easy · recursive + iterative
- [144 · Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) — Easy · root first
- [145 · Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) — Easy · children first
- [102 · Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) — Medium · BFS row by row
- [103 · Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) — Medium · alternate direction per level
- [199 · Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) — Medium · last node in each BFS level

**References**
- [NeetCode · Trees playlist](https://neetcode.io/roadmap)
- [VisuAlgo · BST traversals](https://visualgo.net/en/bst) — step-through inorder/preorder/postorder

## Related
- [[Binary Tree]] — what we're traversing
- [[BST (Binary Search Tree)]] — inorder = sorted output
- [[DFS (Depth-First Search)]] — all traversals except level-order
- [[BFS (Breadth-First Search)]] — level-order traversal
- [[Stack]] — iterative traversals use a stack
