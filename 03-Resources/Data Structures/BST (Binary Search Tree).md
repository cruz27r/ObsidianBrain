---
tags: [concept, data-structure, tree, bst]
created: 2026-03-21
related: [Binary Tree, Tree Traversals, Binary Search]
---

# BST (Binary Search Tree)

## What it is
A binary tree with one critical property: **for every node, all values in its left subtree are less, and all values in its right subtree are greater**.

This isn't just about immediate children — it applies to **all descendants**.

## Complexity
| Operation | Balanced BST | Degenerate (sorted insert) |
|---|---|---|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Min / Max | O(log n) | O(n) |

**Degenerate case**: inserting already-sorted data into a plain BST creates a linked list. Self-balancing BSTs (AVL, Red-Black) prevent this — JS `Map`/`Set` use these internally.

## The killer insight: inorder = sorted
Inorder traversal of any BST yields elements in sorted ascending order. This is used constantly in interview problems.

```typescript
// Kth smallest element in BST
function kthSmallest(root: TreeNode | null, k: number): number {
  let count = 0, result = 0;
  function inorder(node: TreeNode | null) {
    if (!node) return;
    inorder(node.left);
    if (++count === k) { result = node.val; return; }
    inorder(node.right);
  }
  inorder(root);
  return result;
}
```

## Core operations

### Search
```typescript
function search(root: TreeNode | null, target: number): TreeNode | null {
  if (!root || root.val === target) return root;
  return target < root.val ? search(root.left, target) : search(root.right, target);
}
```

### Insert
```typescript
function insert(root: TreeNode | null, val: number): TreeNode {
  if (!root) return new TreeNode(val);
  if (val < root.val) root.left = insert(root.left, val);
  else if (val > root.val) root.right = insert(root.right, val);
  return root; // val === root.val: duplicate, ignore
}
```

### Delete (3 cases)
```typescript
function deleteNode(root: TreeNode | null, key: number): TreeNode | null {
  if (!root) return null;
  if (key < root.val) { root.left = deleteNode(root.left, key); }
  else if (key > root.val) { root.right = deleteNode(root.right, key); }
  else {
    // Found it
    if (!root.left) return root.right;   // Case 1: no left child
    if (!root.right) return root.left;   // Case 2: no right child
    // Case 3: two children — replace with inorder successor (min of right subtree)
    let successor = root.right;
    while (successor.left) successor = successor.left;
    root.val = successor.val;
    root.right = deleteNode(root.right, successor.val);
  }
  return root;
}
```

## Validate BST
Common gotcha: can't just check `left.val < node.val < right.val`. Must check against the valid range for each subtree.
```typescript
function isValidBST(root: TreeNode | null, min = -Infinity, max = Infinity): boolean {
  if (!root) return true;
  if (root.val <= min || root.val >= max) return false;
  return isValidBST(root.left, min, root.val) && isValidBST(root.right, root.val, max);
}
```

## BST vs Hash Map
| | BST | Hash Map |
|---|---|---|
| Lookup | O(log n) | O(1) avg |
| Insert | O(log n) | O(1) avg |
| **Sorted order** | ✅ inorder | ❌ |
| **Range query** | ✅ O(log n + k) | ❌ O(n) |
| **Predecessor/successor** | ✅ | ❌ |

Reach for BST when you need sorted iteration or range queries.

## Multi-Language Reference — BST Search

```javascript
// JavaScript
function search(root, target) {
  if (!root || root.val === target) return root;
  return target < root.val ? search(root.left, target) : search(root.right, target);
}
```

```java
// Java
public TreeNode search(TreeNode root, int target) {
    if (root == null || root.val == target) return root;
    return target < root.val ? search(root.left, target) : search(root.right, target);
}
```

```python
# Python
def search(root, target):
    if not root or root.val == target:
        return root
    return search(root.left, target) if target < root.val else search(root.right, target)
```

```c
// C
struct TreeNode* search(struct TreeNode* root, int target) {
    if (!root || root->val == target) return root;
    return target < root->val ? search(root->left, target) : search(root->right, target);
}
```

```cpp
// C++
TreeNode* search(TreeNode* root, int target) {
    if (!root || root->val == target) return root;
    return target < root->val ? search(root->left, target) : search(root->right, target);
}
```

## Practice & Resources

**LeetCode — Essential Problems**
- [700 · Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) — Easy · pure BST navigation
- [701 · Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/) — Medium · recurse to correct spot
- [98 · Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) — Medium · pass min/max bounds down
- [230 · Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) — Medium · inorder = sorted
- [235 · Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) — Medium · use ordering to decide direction

**References**
- [VisuAlgo · BST](https://visualgo.net/en/bst) — animated insert, delete, search
- [NeetCode · Trees playlist](https://neetcode.io/roadmap)

## Related
- [[Binary Tree]] — BST is a binary tree with ordering
- [[Binary Search]] — same O(log n) intuition
- [[Tree Traversals]] — inorder gives sorted output
