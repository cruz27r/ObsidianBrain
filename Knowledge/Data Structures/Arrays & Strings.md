---
tags: [concept, data-structure, arrays]
created: 2026-03-21
related: [Hash Tables, Two Pointers, Sliding Window]
---

# Arrays & Strings

## What it is
An array is a contiguous block of memory where elements are stored at fixed-size slots. You get O(1) access to any element by index because the address is calculated directly: `base + (index * element_size)`.

Strings in JavaScript/TypeScript are **immutable** — every "modification" creates a new string. This makes string manipulation potentially O(n) even for something that looks trivial.

## Complexity

| Operation | Array | Notes |
|---|---|---|
| Access by index | O(1) | Direct memory calculation |
| Search (unsorted) | O(n) | Linear scan |
| Search (sorted) | O(log n) | [[Binary Search]] |
| Insert/delete at end | O(1) amortized | Arrays grow by doubling |
| Insert/delete at middle | O(n) | Must shift elements |
| String concat in loop | O(n²) | Each `+` copies whole string — use array join |

## Key patterns that use arrays

### 1. Prefix Sums — range queries in O(1) after O(n) setup
```typescript
function buildPrefixSum(nums: number[]): number[] {
  const prefix = [0];
  for (const n of nums) {
    prefix.push(prefix[prefix.length - 1] + n);
  }
  return prefix;
}

// Sum from index l to r (inclusive) = prefix[r+1] - prefix[l]
function rangeSum(prefix: number[], l: number, r: number): number {
  return prefix[r + 1] - prefix[l];
}

// Usage
const nums = [1, 2, 3, 4, 5];
const prefix = buildPrefixSum(nums); // [0, 1, 3, 6, 10, 15]
rangeSum(prefix, 1, 3); // 2+3+4 = 9
```

### 2. In-place reverse — O(n) time, O(1) space
```typescript
function reverseArray<T>(arr: T[]): void {
  let left = 0, right = arr.length - 1;
  while (left < right) {
    [arr[left], arr[right]] = [arr[right], arr[left]];
    left++;
    right--;
  }
}
```

### 3. Kadane's Algorithm — maximum subarray sum O(n)
```typescript
function maxSubarraySum(nums: number[]): number {
  let maxSum = nums[0];
  let currentSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    // Either extend current subarray or start fresh
    currentSum = Math.max(nums[i], currentSum + nums[i]);
    maxSum = Math.max(maxSum, currentSum);
  }
  return maxSum;
}
// [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6 (subarray [4,-1,2,1])
```

### 4. String building — don't use `+` in a loop
```typescript
// ❌ O(n²) — creates new string each iteration
let result = '';
for (const char of chars) result += char;

// ✅ O(n) — join at end
const parts: string[] = [];
for (const char of chars) parts.push(char);
const result = parts.join('');
```

## Common interview mistakes
- **Off-by-one**: `i < arr.length` vs `i <= arr.length - 1` — same thing, but `i <= arr.length` is a bug
- **Mutating while iterating**: causes skipped elements — collect indices first, then remove
- **Forgetting string immutability**: `str[0] = 'x'` silently fails in JS
- **Assuming sorted**: always clarify if input is sorted before reaching for binary search

## Multi-Language Reference — Find Max + Kadane's

```javascript
// JavaScript
const findMax = arr => arr.reduce((max, n) => n > max ? n : max, arr[0]);
function maxSubarraySum(nums) {
  let maxSum = nums[0], curr = nums[0];
  for (let i = 1; i < nums.length; i++) {
    curr = Math.max(nums[i], curr + nums[i]);
    maxSum = Math.max(maxSum, curr);
  }
  return maxSum;
}
```

```java
// Java
public static int findMax(int[] arr) {
    int max = arr[0];
    for (int n : arr) if (n > max) max = n;
    return max;
}
public static int maxSubarraySum(int[] nums) {
    int maxSum = nums[0], curr = nums[0];
    for (int i = 1; i < nums.length; i++) {
        curr = Math.max(nums[i], curr + nums[i]);
        maxSum = Math.max(maxSum, curr);
    }
    return maxSum;
}
// Built-in max: Arrays.stream(arr).max().getAsInt()
```

```python
# Python
def find_max(arr): return max(arr)  # built-in O(n)

def max_subarray_sum(nums):
    max_sum = curr = nums[0]
    for n in nums[1:]:
        curr = max(n, curr + n)
        max_sum = max(max_sum, curr)
    return max_sum
```

```c
// C
int findMax(int arr[], int n) {
    int max = arr[0];
    for (int i = 1; i < n; i++) if (arr[i] > max) max = arr[i];
    return max;
}
int maxSubarraySum(int nums[], int n) {
    int maxSum = nums[0], curr = nums[0];
    for (int i = 1; i < n; i++) {
        curr = nums[i] > curr + nums[i] ? nums[i] : curr + nums[i];
        if (curr > maxSum) maxSum = curr;
    }
    return maxSum;
}
```

```cpp
// C++
int findMax(vector<int>& arr) { return *max_element(arr.begin(), arr.end()); }
int maxSubarraySum(vector<int>& nums) {
    int maxSum = nums[0], curr = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        curr = max(nums[i], curr + nums[i]);
        maxSum = max(maxSum, curr);
    }
    return maxSum;
}
```

## Practice & Resources

**LeetCode — Essential Problems**
- [217 · Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) — Easy · hash set warm-up
- [121 · Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) — Easy · track running min
- [53 · Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) — Medium · Kadane's algorithm
- [238 · Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) — Medium · prefix + suffix products
- [56 · Merge Intervals](https://leetcode.com/problems/merge-intervals/) — Medium · sort + merge
- [42 · Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) — Hard · prefix max arrays

**References**
- [NeetCode · Arrays & Hashing playlist](https://neetcode.io/roadmap)
- [VisuAlgo · Sorting / Array visualizations](https://visualgo.net/en/sorting)

## Related
- [[Two Pointers]] — most array problems use two pointers
- [[Sliding Window]] — subarray/substring problems
- [[Hash Tables]] — when you need O(1) lookup by value
- [[Binary Search]] — for sorted arrays
