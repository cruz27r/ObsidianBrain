---
tags: [concept, algorithm, greedy]
created: 2026-03-21
related: [Dynamic Programming, Sorting Algorithms, Heap (Priority Queue)]
---

# Greedy

## What It Is

A greedy algorithm makes the locally optimal choice at each step — the choice that looks best right now — without reconsidering past decisions. The goal is that a sequence of locally optimal choices leads to a globally optimal solution.

The word "greedy" is descriptive: the algorithm greedily grabs the best available option at each moment and never gives it back.

```
Example: making change with coins [25, 10, 5, 1] for 41 cents
Greedy: take largest coin that fits each time
→ 25, 10, 5, 1 = 4 coins

This is optimal for standard US coin denominations.
But greedy fails for coins [1, 3, 4] and amount 6:
→ Greedy: 4 + 1 + 1 = 3 coins
→ Optimal: 3 + 3 = 2 coins
```

---

## Greedy vs Dynamic Programming

| | Greedy | [[Dynamic Programming]] |
|---|---|---|
| **Reconsiders choices?** | Never | Yes — explores all options |
| **Speed** | Faster (often O(n log n)) | Slower (polynomial, sometimes exponential states) |
| **When it works** | Only when greedy choice property holds | Always when optimal substructure holds |
| **Proof required?** | Yes — must prove greedy is safe | No — correctness follows from recurrence |
| **Example** | Activity selection, Dijkstra | Knapsack, LCS, coin change |

**Greedy choice property**: a globally optimal solution can always be constructed by making locally optimal choices. This must be proven — you can't just assume greedy works.

**When greedy fails**: when an early "optimal" choice blocks better options later. The 0/1 knapsack is the classic example — taking the most valuable item first may prevent filling the remaining capacity optimally.

---

## How to Recognize Greedy Problems

- **Interval scheduling**: "select maximum number of non-overlapping intervals"
- **Sorting-based decisions**: the right sort order reveals the greedy choice
- **"Always pick the best available"**: largest/smallest item, earliest deadline, most/least costly
- **Local choices don't create future regrets**: making the best choice now never makes things worse later

**Proof technique — exchange argument**: assume a non-greedy optimal solution exists. Show you can swap any non-greedy choice with the greedy choice and the solution doesn't get worse. Therefore the greedy solution is also optimal.

---

## TypeScript Examples

### Activity Selection / Non-Overlapping Intervals

Find the maximum number of non-overlapping intervals (equivalently, minimum removals to make all intervals non-overlapping).

**Greedy choice**: always pick the interval that ends earliest. This leaves the most room for future intervals.

```typescript
function eraseOverlapIntervals(intervals: number[][]): number {
  if (intervals.length === 0) return 0;

  // sort by end time — greedy choice is earliest ending interval
  intervals.sort((a, b) => a[1] - b[1]);

  let removals = 0;
  let lastEnd = intervals[0][1];

  for (let i = 1; i < intervals.length; i++) {
    if (intervals[i][0] < lastEnd) {
      // overlap: remove current interval (it ends later, so keeping it is worse)
      removals++;
    } else {
      // no overlap: keep it, update lastEnd
      lastEnd = intervals[i][1];
    }
  }

  return removals;
}

// eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) => 1  (remove [1,3])
// eraseOverlapIntervals([[1,2],[1,2],[1,2]]) => 2
```

**Exchange argument**: suppose optimal keeps an interval that ends later than the greedy choice. We can swap it for the greedy (earlier ending) interval — this can only free up more future space, so the solution is at least as good.

---

### Jump Game

Given an array where each element is your max jump length from that position, can you reach the last index?

**Greedy choice**: track the farthest index reachable at each step. If you pass through an unreachable index, return false.

```typescript
function canJump(nums: number[]): boolean {
  let maxReach = 0;

  for (let i = 0; i < nums.length; i++) {
    if (i > maxReach) return false; // can't reach this position

    maxReach = Math.max(maxReach, i + nums[i]);

    if (maxReach >= nums.length - 1) return true;
  }

  return true;
}

// canJump([2,3,1,1,4]) => true
// canJump([3,2,1,0,4]) => false  (stuck at index 3)
```

**Why greedy works**: at each position, the greedy choice is to keep track of the maximum reachable index. If position `i` is reachable (i ≤ maxReach), we update maxReach. There's no reason to be conservative — the farther you can reach, the more options you have.

**Variation — Jump Game II (minimum jumps)**:

```typescript
function jump(nums: number[]): number {
  let jumps = 0;
  let currentEnd = 0;  // farthest index reachable with `jumps` jumps
  let farthest = 0;    // farthest reachable from any position in current range

  for (let i = 0; i < nums.length - 1; i++) {
    farthest = Math.max(farthest, i + nums[i]);

    if (i === currentEnd) {
      // must make a jump — choose the position that reaches farthest
      jumps++;
      currentEnd = farthest;
    }
  }

  return jumps;
}

// jump([2,3,1,1,4]) => 2  (0→1→4 or 0→1→4)
```

---

### Gas Station

Can you complete a circular route? If yes, where to start?

**Greedy insight**: if total gas >= total cost, a solution always exists. The starting station is the one after the last point where the running tank went negative.

```typescript
function canCompleteCircuit(gas: number[], cost: number[]): number {
  let totalGas = 0;
  let currentGas = 0;
  let start = 0;

  for (let i = 0; i < gas.length; i++) {
    const net = gas[i] - cost[i];
    totalGas += net;
    currentGas += net;

    if (currentGas < 0) {
      // can't reach i+1 from current start; try starting from i+1
      start = i + 1;
      currentGas = 0;
    }
  }

  // if total gas >= total cost, a solution exists and it's at `start`
  return totalGas >= 0 ? start : -1;
}

// canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) => 3
// canCompleteCircuit([2,3,4], [3,4,3]) => -1
```

**Why this works**: if you run out of gas at station `k`, you can't start from any station between `start` and `k` (they all had enough gas to reach each other, and adding a deficit station before them only makes things worse). So the next candidate start is `k+1`.

---

### Assign Cookies

Each child needs a minimum cookie size. Each cookie can only be given to one child. Maximize the number of content children.

**Greedy choice**: sort both arrays. Give the smallest sufficient cookie to the least greedy child.

```typescript
function findContentChildren(g: number[], s: number[]): number {
  g.sort((a, b) => a - b); // child greediness (ascending)
  s.sort((a, b) => a - b); // cookie sizes (ascending)

  let child = 0;
  let cookie = 0;

  while (child < g.length && cookie < s.length) {
    if (s[cookie] >= g[child]) {
      child++; // child is satisfied
    }
    cookie++; // try next cookie regardless
  }

  return child;
}

// findContentChildren([1,2,3], [1,1]) => 1
// findContentChildren([1,2], [1,2,3]) => 2
```

**Exchange argument**: suppose optimal assigns a large cookie to a less greedy child. We can always swap it with the smallest sufficient cookie for that child, freeing the large cookie for a greedier child — result is at least as good.

---

## Proving Greedy Correctness

When you propose a greedy solution in an interview, be ready to justify it:

1. **Define the greedy choice**: precisely state what "locally optimal" means for this problem
2. **State the greedy choice property**: "making this choice at step k never prevents an optimal solution for steps k+1 onward"
3. **Exchange argument**: "assume optimal makes a different choice at some step. We can swap it for the greedy choice. The new solution is no worse. Therefore greedy is also optimal."

If you can't articulate why greedy is safe, you probably need DP instead.

---

## Common Mistakes

- **Greedy without proof**: not every "obvious" local choice leads to global optimum (coin change with unusual denominations fails greedy)
- **Wrong sort order**: sorting by start time instead of end time in interval problems gives the wrong answer
- **Forgetting ties**: when two choices are equally good locally, a tie-breaking rule may matter for correctness
- **Confusing greedy with DP**: if the problem has "how many ways" or requires exploring alternatives, it's likely DP

---

## Multi-Language Reference — Jump Game

```javascript
// JavaScript
function canJump(nums) {
  let maxReach = 0;
  for (let i = 0; i < nums.length; i++) {
    if (i > maxReach) return false;
    maxReach = Math.max(maxReach, i + nums[i]);
  }
  return true;
}
```

```java
// Java
public static boolean canJump(int[] nums) {
    int maxReach = 0;
    for (int i = 0; i < nums.length; i++) {
        if (i > maxReach) return false;
        maxReach = Math.max(maxReach, i + nums[i]);
    }
    return true;
}
```

```python
# Python
def can_jump(nums):
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach: return False
        max_reach = max(max_reach, i + jump)
    return True
```

```c
// C
int canJump(int nums[], int n) {
    int maxReach = 0;
    for (int i = 0; i < n; i++) {
        if (i > maxReach) return 0;
        if (i + nums[i] > maxReach) maxReach = i + nums[i];
    }
    return 1;
}
```

```cpp
// C++
bool canJump(vector<int>& nums) {
    int maxReach = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (i > maxReach) return false;
        maxReach = max(maxReach, i + nums[i]);
    }
    return true;
}
```

## Practice & Resources

**LeetCode — Essential Problems**
- [455 · Assign Cookies](https://leetcode.com/problems/assign-cookies/) — Easy · warm-up
- [55 · Jump Game](https://leetcode.com/problems/jump-game/) — Medium · track max reachable
- [45 · Jump Game II](https://leetcode.com/problems/jump-game-ii/) — Medium · minimum jumps
- [134 · Gas Station](https://leetcode.com/problems/gas-station/) — Medium · circular greedy
- [435 · Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) — Medium · sort by end time
- [763 · Partition Labels](https://leetcode.com/problems/partition-labels/) — Medium · last occurrence tracking

**References**
- [NeetCode · Greedy playlist](https://neetcode.io/roadmap)

## Related

- [[Dynamic Programming]]
- [[Sorting Algorithms]]
- [[Heap (Priority Queue)]]
