---
tags: [concept, algorithm, searching]
created: 2026-03-21
related: [Big O Notation, Sorting Algorithms]
---

# Binary Search

## What it is
A search algorithm that finds a target in a **sorted** array by repeatedly halving the search range. Much faster than scanning every element.

## Complexity
| | |
|---|---|
| Time | O(log n) |
| Space | O(1) iterative / O(log n) recursive |

With 1 million items: linear search = up to 1,000,000 checks. Binary search = at most 20.

## When to use it
- Array is sorted (required — won't work otherwise)
- You need fast lookups by value
- Searching large datasets

## When NOT to use it
- Unsorted data (sort first, or use a [[Hash Tables|hash map]] instead)
- [[Linked List|Linked lists]] — no O(1) index access, kills the advantage

## How it works
1. Start with low = 0, high = last index
2. Find mid = Math.floor((low + high) / 2)
3. If arr[mid] === target → found
4. If arr[mid] < target → search right half (low = mid + 1)
5. If arr[mid] > target → search left half (high = mid - 1)
6. Repeat until found or low > high

## Process Flow

```mermaid
flowchart TD
    classDef init fill:#1e3a5f,stroke:none,color:#fff
    classDef step fill:#1d4ed8,stroke:none,color:#fff
    classDef found fill:#166534,stroke:none,color:#fff
    classDef miss fill:#374151,stroke:none,color:#f9fafb
    A(["low = 0  ·  high = n−1"]):::init --> B{low ≤ high?}
    B -->|No| MISS(["Return −1  · not found"]):::miss
    B -->|Yes| C["mid = ⌊(low + high) / 2⌋"]:::step
    C --> D{arr[mid] vs target?}
    D -->|Equal| FOUND(["Return mid"]):::found
    D -->|arr[mid] < target| E["low = mid + 1  · search right"]:::step
    D -->|arr[mid] > target| F["high = mid − 1  · search left"]:::step
    E --> B
    F --> B
```

*Why this is O(log n): each iteration cuts the remaining search space in half. 1,000,000 → 500,000 → 250,000 → ... → 1. That's only 20 steps.*

## Code (TypeScript)
```typescript
function binarySearch(arr: number[], target: number): number {
  let low = 0;
  let high = arr.length - 1;

  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) low = mid + 1;
    else high = mid - 1;
  }

  return -1; // not found
}

// Usage
const sorted = [1, 3, 5, 7, 9, 11, 13];
binarySearch(sorted, 7);  // → 3 (index)
binarySearch(sorted, 6);  // → -1
```

## Multi-Language Reference

```javascript
// JavaScript
function binarySearch(arr, target) {
  let low = 0, high = arr.length - 1;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    if (arr[mid] === target) return mid;
    arr[mid] < target ? low = mid + 1 : high = mid - 1;
  }
  return -1;
}
```

```java
// Java
public static int binarySearch(int[] arr, int target) {
    int low = 0, high = arr.length - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2; // avoids overflow vs (low+high)/2
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
// Built-in: Arrays.binarySearch(arr, target)
```

```python
# Python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: low = mid + 1
        else: high = mid - 1
    return -1

# Built-in: import bisect; bisect.bisect_left(arr, target)
```

```c
// C
int binarySearch(int arr[], int n, int target) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
// Built-in: bsearch() from stdlib.h
```

```cpp
// C++
int binarySearch(vector<int>& arr, int target) {
    int low = 0, high = arr.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
// Built-in: lower_bound(arr.begin(), arr.end(), target)
```

## Practice & Resources

**LeetCode — Essential Problems**
- [704 · Binary Search](https://leetcode.com/problems/binary-search/) — Easy · the baseline
- [153 · Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) — Medium · apply to unsorted
- [33 · Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) — Medium · classic twist
- [875 · Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) — Medium · binary search on answer
- [4 · Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) — Hard · canonical hard problem

**References**
- [NeetCode · Binary Search playlist](https://neetcode.io/roadmap) — video walkthroughs for every pattern
- [VisuAlgo · Binary Search](https://visualgo.net/en/bst) — step-by-step animation

## Related
- [[Big O Notation]] — why O(log n) matters
- [[Sorting Algorithms]] — data must be sorted first
