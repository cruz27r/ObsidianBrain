---
tags: [concept, algorithm, pattern]
created: 2026-03-21
related: [Linked List, Arrays & Strings, Two Pointers]
---

# Fast & Slow Pointers

## What It Is

Fast & slow pointers (also called Floyd's Tortoise and Hare algorithm) uses two pointers that traverse a sequence at different speeds — typically `slow` moves one step at a time, `fast` moves two steps at a time.

The key insight: if a sequence contains a cycle, the fast pointer will eventually lap the slow pointer and they will meet inside the cycle. If there is no cycle, the fast pointer will reach the end first.

This gives O(n) time and O(1) space — no visited set needed.

---

## Why It Works for Cycle Detection

Think of two runners on a circular track. The faster runner will always eventually lap the slower one, no matter how large the track is. Once they're both inside the cycle, the gap between them decreases by 1 on each step (fast closes 1 step per iteration since it moves 2 and slow moves 1). So they must meet within at most `cycle_length` steps after fast enters the cycle.

```
List:  1 → 2 → 3 → 4 → 5
                    ↑       ↓
                    8 ← 7 ← 6

slow: 1 → 2 → 3 → 4 → 5 → 6 → 7 ...
fast: 1 → 3 → 5 → 7 → 4 → 6 → 8 ...
          ↑ eventually they meet
```

---

## When to Use

- Detect a cycle in a [[Linked List|linked list]] or numeric sequence
- Find the start of a cycle
- Find the middle of a linked list (in one pass)
- Check if a linked list is a palindrome (find middle, reverse second half)
- Happy number problem (detect if a sequence loops)

**Dead giveaway**: "detect cycle", "find middle", "is there a loop", "Floyd's"

---

## TypeScript Examples

### Detect Cycle in Linked List

```typescript
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val: number, next: ListNode | null = null) {
    this.val = val;
    this.next = next;
  }
}

function hasCycle(head: ListNode | null): boolean {
  let slow = head;
  let fast = head;

  while (fast !== null && fast.next !== null) {
    slow = slow!.next;          // move 1 step
    fast = fast.next.next;      // move 2 steps

    if (slow === fast) {
      return true; // cycle detected — they met
    }
  }

  return false; // fast reached end → no cycle
}
```

**Termination conditions**: if `fast` or `fast.next` is null, we've reached the end of the list — no cycle. The `fast.next !== null` check is needed because fast moves two steps; we must ensure the second step is valid.

---

### Find Start of Cycle

After detecting a cycle (slow and fast meet), reset one pointer to `head`. Then advance both one step at a time — they will meet exactly at the cycle start.

```typescript
function detectCycleStart(head: ListNode | null): ListNode | null {
  let slow = head;
  let fast = head;

  // phase 1: detect cycle
  while (fast !== null && fast.next !== null) {
    slow = slow!.next;
    fast = fast.next.next;

    if (slow === fast) {
      // phase 2: find cycle start
      // reset slow to head; keep fast at meeting point
      slow = head;

      while (slow !== fast) {
        slow = slow!.next;
        fast = fast!.next; // now both move 1 step
      }

      return slow; // this is the cycle start
    }
  }

  return null; // no cycle
}
```

**Why this works (the math)**: let `F` = distance from head to cycle start, `C` = cycle length, `a` = distance from cycle start to meeting point. When they meet: slow has traveled `F + a`, fast has traveled `F + a + C` (it lapped). Since fast moves 2x: `2(F + a) = F + a + C`, which gives `F = C - a`. So the distance from head to cycle start equals the remaining distance from the meeting point back around to the cycle start. Walking one step at a time from both head and meeting point, they arrive at cycle start simultaneously.

---

### Find Middle of Linked List

When `fast` reaches the end, `slow` is at the middle. For even-length lists, `slow` lands on the second middle node.

```typescript
function findMiddle(head: ListNode | null): ListNode | null {
  let slow = head;
  let fast = head;

  while (fast !== null && fast.next !== null) {
    slow = slow!.next;
    fast = fast.next.next;
  }

  return slow; // middle node
}

// List: 1 → 2 → 3 → 4 → 5
// Returns node with val=3

// List: 1 → 2 → 3 → 4
// Returns node with val=3 (second of two middle nodes)
```

**Variation**: if you want the first middle of an even list, check `fast.next.next !== null` instead, so fast stops one step earlier.

---

### Happy Number

A happy number repeatedly sums the squares of its digits. If it reaches 1, it's happy. If it cycles (never reaches 1), it's not. Use fast & slow to detect the cycle.

```typescript
function isHappy(n: number): boolean {
  function sumOfSquares(num: number): number {
    let sum = 0;
    while (num > 0) {
      const digit = num % 10;
      sum += digit * digit;
      num = Math.floor(num / 10);
    }
    return sum;
  }

  let slow = n;
  let fast = n;

  do {
    slow = sumOfSquares(slow);             // 1 step
    fast = sumOfSquares(sumOfSquares(fast)); // 2 steps
  } while (slow !== fast);

  // if they met at 1, it's happy; otherwise they met in a cycle
  return slow === 1;
}

// isHappy(19) => true  (19 → 82 → 68 → 100 → 1)
// isHappy(2) => false  (cycles: 2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 ...)
```

**Key insight**: treating each number as a "node" and the next digit-square-sum as "next", the sequence either terminates at 1 or forms a cycle. Fast & slow detects both without a hash set.

---

## Complexity

| Problem | Time | Space |
|---|---|---|
| Detect cycle | O(n) | O(1) |
| Find cycle start | O(n) | O(1) |
| Find middle | O(n) | O(1) |
| Happy number | O(log n) per step × O(cycle length) | O(1) |

The O(1) space is the main advantage over using a visited hash set (which would be O(n)).

---

## Common Mistakes

- **Forgetting `fast.next !== null`** before `fast.next.next` — this will throw a null pointer error
- **Using `do...while` vs `while`**: for cycle detection where `slow` and `fast` start at the same node, you need at least one step before checking; `do...while` handles this naturally
- **Phase 2 pointer placement**: reset `slow` to `head`, but keep `fast` exactly at the meeting point — do not reset `fast`
- **Off-by-one in middle finding**: for even lists, which "middle" you want depends on whether you check `fast.next !== null` or `fast.next.next !== null`

---

## Multi-Language Reference — Detect Cycle in Linked List

```javascript
// JavaScript
function hasCycle(head) {
  let slow = head, fast = head;
  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
}
```

```java
// Java
public static boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}
```

```python
# Python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

```c
// C
int hasCycle(struct ListNode* head) {
    struct ListNode *slow = head, *fast = head;
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return 1;
    }
    return 0;
}
```

```cpp
// C++
bool hasCycle(ListNode* head) {
    ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}
```

## Practice & Resources

**LeetCode — Essential Problems**
- [141 · Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) — Easy · classic fast & slow
- [876 · Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) — Easy · slow stops at middle
- [202 · Happy Number](https://leetcode.com/problems/happy-number/) — Easy · cycle detection on digit sums
- [142 · Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) — Medium · find cycle entry point
- [287 · Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) — Medium · Floyd's on array-as-linked-list

**References**
- [NeetCode · Linked List playlist](https://neetcode.io/roadmap)
- [VisuAlgo · Linked List](https://visualgo.net/en/list) — pointer visualization

## Related

- [[Linked List]]
- [[Two Pointers]]
