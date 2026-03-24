---
tags: [concept, algorithm, complexity]
created: 2026-03-21
related: [Binary Search, Sorting Algorithms, Hash Tables]
---

# Big O Notation

## What it is
A way to describe how the performance of an algorithm scales as input size grows. You're not measuring exact time — you're measuring the *shape* of how it gets worse (or stays the same).

## Common Complexities (best → worst)

| Notation | Name | Example |
|---|---|---|
| O(1) | Constant | [[Arrays & Strings|Array]] index lookup, [[Hash Tables|hash map]] get |
| O(log n) | Logarithmic | [[Binary Search]] |
| O(n) | Linear | Loop through array once |
| O(n log n) | Linearithmic | Merge sort, [[Sorting Algorithms|heap sort]] |
| O(n²) | Quadratic | Nested loops (bubble sort) |
| O(2ⁿ) | Exponential | Recursive Fibonacci (naive) |
| O(n!) | Factorial | Permutations of n items |

## How it works
Drop constants and lower-order terms. You care about what dominates at scale:
- `3n + 100` → **O(n)**
- `n² + n` → **O(n²)**
- `5` → **O(1)**

Space complexity follows the same rules but for memory usage instead of time.

## How we use it
When writing or reviewing code — ask: "what's the worst case as data grows?" A function that loops inside a loop on the same array is O(n²) — fine for 100 items, brutal for 100,000.

```typescript
// O(n) — one pass
function findMax(arr: number[]): number {
  let max = arr[0];
  for (const n of arr) {
    if (n > max) max = n;
  }
  return max;
}

// O(n²) — nested loops on same data
function hasDuplicate(arr: number[]): boolean {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] === arr[j]) return true;
    }
  }
  return false;
}

// O(n) version using a Set
function hasDuplicateFast(arr: number[]): boolean {
  return new Set(arr).size !== arr.length;
}
```

## Multi-Language Reference
Same O(n) linear scan and O(n) dedup — shown in every language.

```javascript
// JavaScript
function findMax(arr) {
  let max = arr[0];
  for (const n of arr) { if (n > max) max = n; }
  return max;
}
function hasDuplicateFast(arr) {
  return new Set(arr).size !== arr.length; // O(n)
}
```

```java
// Java
public static int findMax(int[] arr) {
    int max = arr[0];
    for (int n : arr) { if (n > max) max = n; }
    return max;
}
public static boolean hasDuplicate(int[] arr) {
    Set<Integer> seen = new HashSet<>();
    for (int n : arr) { if (!seen.add(n)) return true; }
    return false;
}
```

```python
# Python
def find_max(arr):
    return max(arr)  # built-in is O(n)

def has_duplicate(arr):
    return len(arr) != len(set(arr))  # O(n)
```

```c
// C
int findMax(int arr[], int n) {
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) max = arr[i];
    }
    return max;
}
// No built-in set in C — O(n²) duplicate check or sort first
int hasDuplicate(int arr[], int n) {
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (arr[i] == arr[j]) return 1;
    return 0;
}
```

```cpp
// C++
int findMax(vector<int>& arr) {
    return *max_element(arr.begin(), arr.end()); // O(n)
}
bool hasDuplicate(vector<int>& arr) {
    return unordered_set<int>(arr.begin(), arr.end()).size() != arr.size();
}
```

## Practice & Resources

**References**
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) — complexity of every common algorithm and data structure at a glance
- [NeetCode · Roadmap](https://neetcode.io/roadmap) — organized by pattern, each with complexity analysis
- [CS50 · Computational Complexity lecture](https://cs50.harvard.edu/x/) — free, beginner-friendly video

## Related
- [[Binary Search]] — example of O(log n) in practice
- [[Sorting Algorithms]] — comparing O(n log n) vs O(n²) sorts
- [[Hash Tables]] — why O(1) average lookup matters
