---
tags: [concept, algorithm, recursion]
created: 2026-03-21
related: [Sorting Algorithms, Binary Search, Dynamic Programming]
---

# Divide & Conquer

## What It Is

Divide & conquer solves a problem by:
1. **Divide**: split the problem into smaller subproblems of the same type
2. **Conquer**: solve each subproblem recursively (base case when small enough)
3. **Combine**: merge the subproblem solutions into a solution for the original problem

The subproblems are **independent** — they don't share state or overlap. This is the key distinction from DP.

```
Merge Sort (divide & conquer):
[3, 1, 4, 1, 5, 9, 2, 6]
         ↓ divide
[3, 1, 4, 1]  [5, 9, 2, 6]
      ↓              ↓  (recurse)
[3,1] [4,1]    [5,9] [2,6]
  ↓      ↓       ↓     ↓
[1,3] [1,4]   [5,9] [2,6]
      ↓ combine
[1, 1, 3, 4]  [2, 5, 6, 9]
              ↓ combine
      [1, 1, 2, 3, 4, 5, 6, 9]
```

---

## Divide & Conquer vs Dynamic Programming

| | Divide & Conquer | Dynamic Programming |
|---|---|---|
| **Subproblems** | Independent (no overlap) | Overlapping (same subproblem computed multiple times) |
| **Caching needed?** | No — each subproblem solved once naturally | Yes — memoization or tabulation required |
| **Typical time** | O(n log n) | O(n²) or better with optimization |
| **Examples** | Merge sort, quick sort, binary search | Fibonacci, LCS, knapsack |

If you run a divide & conquer algorithm on a problem with overlapping subproblems (e.g., naive Fibonacci), it degenerates to exponential time. The fix is memoization → now you have DP.

---

## The Master Theorem

Most divide & conquer algorithms have a recurrence of the form:

```
T(n) = a·T(n/b) + f(n)
```

Where:
- `a` = number of subproblems
- `n/b` = size of each subproblem
- `f(n)` = cost of dividing and combining

**Three cases** (simplified):

| Case | Condition | Result |
|---|---|---|
| **Case 1** | `f(n) = O(n^c)` where `c < log_b(a)` | `T(n) = Θ(n^log_b(a))` — recursion dominates |
| **Case 2** | `f(n) = Θ(n^log_b(a))` | `T(n) = Θ(n^log_b(a) · log n)` — tied |
| **Case 3** | `f(n) = Ω(n^c)` where `c > log_b(a)` | `T(n) = Θ(f(n))` — combining dominates |

**Applied to merge sort**: `T(n) = 2T(n/2) + O(n)`
- a=2, b=2, `log_b(a) = log_2(2) = 1`, `f(n) = O(n) = O(n^1)`
- `c = 1 = log_b(a)` → Case 2 → `T(n) = Θ(n log n)` ✓

**Applied to binary search**: `T(n) = T(n/2) + O(1)`
- a=1, b=2, `log_b(a) = 0`, `f(n) = O(1) = O(n^0)`
- `c = 0 = log_b(a)` → Case 2 → `T(n) = Θ(log n)` ✓

---

## Classic Examples

All three are divide & conquer:

- **Binary search**: divide search space in half, conquer one half, no combine step
- **Merge sort**: divide array in half, conquer both halves, combine with merge
- **Quick sort**: divide by partition (pivot), conquer both partitions, no combine step

See [[Sorting Algorithms]] for merge sort and quick sort implementations.

---

## TypeScript Examples

### Maximum Subarray (Divide & Conquer)

Kadane's algorithm (greedy/DP) gives O(n), but divide & conquer gives O(n log n) and is a common D&C exercise.

**Insight**: the maximum subarray either lies entirely in the left half, entirely in the right half, or crosses the midpoint. For the crossing case, find the max suffix of the left half and max prefix of the right half — their sum is the max crossing subarray.

```typescript
function maxSubarray(nums: number[]): number {
  function maxCrossingSum(left: number, mid: number, right: number): number {
    // max suffix of left half (must include nums[mid])
    let leftMax = -Infinity;
    let sum = 0;
    for (let i = mid; i >= left; i--) {
      sum += nums[i];
      leftMax = Math.max(leftMax, sum);
    }

    // max prefix of right half (must include nums[mid+1])
    let rightMax = -Infinity;
    sum = 0;
    for (let i = mid + 1; i <= right; i++) {
      sum += nums[i];
      rightMax = Math.max(rightMax, sum);
    }

    return leftMax + rightMax;
  }

  function solve(left: number, right: number): number {
    if (left === right) return nums[left]; // base case: single element

    const mid = Math.floor((left + right) / 2);

    return Math.max(
      solve(left, mid),       // max in left half
      solve(mid + 1, right),  // max in right half
      maxCrossingSum(left, mid, right) // max crossing midpoint
    );
  }

  return solve(0, nums.length - 1);
}

// maxSubarray([-2,1,-3,4,-1,2,1,-5,4]) => 6  ([4,-1,2,1])
// maxSubarray([1]) => 1
// maxSubarray([-1,-2,-3]) => -1
```

**Complexity**: T(n) = 2T(n/2) + O(n) → O(n log n) by Master Theorem Case 2. Note: Kadane's O(n) is better in practice — this is an academic D&C example.

---

### Count Inversions in Array

An inversion is a pair (i, j) where i < j but nums[i] > nums[j]. Count all inversions.

**Key insight**: merge sort naturally counts inversions. When merging two sorted halves, if `left[i] > right[j]`, then `left[i]` is greater than all remaining elements in right (since right is sorted) — those are all inversions.

```typescript
function countInversions(nums: number[]): number {
  let inversions = 0;

  function mergeSort(arr: number[]): number[] {
    if (arr.length <= 1) return arr;

    const mid = Math.floor(arr.length / 2);
    const left = mergeSort(arr.slice(0, mid));
    const right = mergeSort(arr.slice(mid));

    return merge(left, right);
  }

  function merge(left: number[], right: number[]): number[] {
    const result: number[] = [];
    let i = 0, j = 0;

    while (i < left.length && j < right.length) {
      if (left[i] <= right[j]) {
        result.push(left[i++]);
      } else {
        // left[i] > right[j]: all remaining elements in left are > right[j]
        inversions += left.length - i; // count them all
        result.push(right[j++]);
      }
    }

    // append remainders
    while (i < left.length) result.push(left[i++]);
    while (j < right.length) result.push(right[j++]);

    return result;
  }

  mergeSort(nums);
  return inversions;
}

// countInversions([3, 1, 2]) => 2  ((3,1) and (3,2))
// countInversions([1, 2, 3]) => 0  (already sorted)
// countInversions([3, 2, 1]) => 3  (all pairs are inversions)
```

**Why this is O(n log n)**: merge sort is O(n log n) and the inversion counting adds O(1) work per merge step. Total: O(n log n).

**Real-world use**: counting inversions measures how "unsorted" an array is. Used in algorithms for comparing rankings (e.g., Kendall tau distance).

---

## The D&C Template

```typescript
function divideAndConquer(problem: Problem): Solution {
  // base case: problem small enough to solve directly
  if (problem.isSmall()) {
    return problem.solveDirect();
  }

  // divide: split into independent subproblems
  const [sub1, sub2] = problem.split();

  // conquer: solve recursively
  const sol1 = divideAndConquer(sub1);
  const sol2 = divideAndConquer(sub2);

  // combine: merge subproblem solutions
  return combine(sol1, sol2);
}
```

---

## Complexity Summary

| Algorithm | Recurrence | Time |
|---|---|---|
| Binary search | T(n) = T(n/2) + O(1) | O(log n) |
| Merge sort | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Quick sort (avg) | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Quick sort (worst) | T(n) = T(n-1) + O(n) | O(n²) |
| Max subarray (D&C) | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Count inversions | T(n) = 2T(n/2) + O(n) | O(n log n) |

---

## Common Mistakes

- **Confusing with DP**: if subproblems overlap and you're recomputing the same inputs, you need memoization (→ DP)
- **Off-by-one in midpoint**: always use `Math.floor((left + right) / 2)` to avoid overflow and ensure correct split
- **Forgetting the combine step**: binary search has no combine step; merge sort has an O(n) combine step — know which applies
- **Worst-case quick sort**: naive pivot selection (always first/last element) gives O(n²) on sorted input. Use random pivot or median-of-three.

---

## Multi-Language Reference — Binary Search (D&C form)

```javascript
// JavaScript (recursive D&C form)
function binarySearch(arr, target, low = 0, high = arr.length - 1) {
  if (low > high) return -1;
  const mid = Math.floor((low + high) / 2);
  if (arr[mid] === target) return mid;
  return arr[mid] < target
    ? binarySearch(arr, target, mid + 1, high)
    : binarySearch(arr, target, low, mid - 1);
}
```

```java
// Java
public static int binarySearch(int[] arr, int target, int low, int high) {
    if (low > high) return -1;
    int mid = low + (high - low) / 2;
    if (arr[mid] == target) return mid;
    return arr[mid] < target
        ? binarySearch(arr, target, mid + 1, high)
        : binarySearch(arr, target, low, mid - 1);
}
```

```python
# Python
def binary_search(arr, target, low=0, high=None):
    if high is None: high = len(arr) - 1
    if low > high: return -1
    mid = (low + high) // 2
    if arr[mid] == target: return mid
    if arr[mid] < target: return binary_search(arr, target, mid + 1, high)
    return binary_search(arr, target, low, mid - 1)
```

```c
// C
int binarySearch(int arr[], int low, int high, int target) {
    if (low > high) return -1;
    int mid = low + (high - low) / 2;
    if (arr[mid] == target) return mid;
    if (arr[mid] < target) return binarySearch(arr, mid + 1, high, target);
    return binarySearch(arr, low, mid - 1, target);
}
```

```cpp
// C++
int binarySearch(vector<int>& arr, int low, int high, int target) {
    if (low > high) return -1;
    int mid = low + (high - low) / 2;
    if (arr[mid] == target) return mid;
    if (arr[mid] < target) return binarySearch(arr, mid + 1, high, target);
    return binarySearch(arr, low, mid - 1, target);
}
```

## Practice & Resources

**LeetCode — Essential Problems**
- [53 · Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) — Medium · D&C solution (Kadane's is simpler, but D&C is instructive)
- [148 · Sort List](https://leetcode.com/problems/sort-list/) — Medium · merge sort on linked list
- [215 · Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) — Medium · quickselect (D&C)
- [4 · Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) — Hard · binary search D&C, O(log(m+n))

**References**
- [NeetCode · Advanced algorithms playlist](https://neetcode.io/roadmap)
- [Khan Academy · D&C](https://www.khanacademy.org/computing/computer-science/algorithms) — visual merge sort walkthrough

## Related

- [[Sorting Algorithms]]
- [[Binary Search]]
- [[Dynamic Programming]]
