---
tags: [concept, algorithm, bits]
created: 2026-03-21
related: [Arrays & Strings, Dynamic Programming]
---

> [!pattern] Bitwise · XOR Tricks

# Bit Manipulation

## Why It Matters

Bit manipulation lets you perform operations directly on binary representations of numbers. The payoffs in interviews:

- **O(1) space** tricks that replace hash sets or extra [[Arrays & Strings|arrays]]
- **XOR-based** solutions for "find the unique element" class of problems
- Fast modular arithmetic (powers of 2, even/odd checks)
- Masking and flag patterns common in systems/embedded questions

Modern JS/TS bitwise operators work on 32-bit signed integers. Be aware: `~n = -(n+1)` due to two's complement.

---

## Key Operations

### AND (`&`) — Mask Bits / Check If Bit Is Set

AND produces a 1 only when both bits are 1. Use it to isolate or check specific bits.

```
  1010
& 1100
------
  1000   ← only bits set in both operands survive
```

**Check if bit i is set**: `(n >> i) & 1` — shift bit i to position 0, then AND with 1
**Mask lower k bits**: `n & ((1 << k) - 1)` — creates a mask of k ones

### OR (`|`) — Set a Bit

OR produces a 1 when at least one bit is 1. Use it to turn a bit on.

```
  1010
| 0101
------
  1111   ← any bit set in either operand is set in result
```

**Set bit i**: `n | (1 << i)` — creates a mask with only bit i set, then OR

### XOR (`^`) — Toggle / Find Unique

XOR produces a 1 when bits differ. Two key properties make it powerful:
- `x ^ x = 0` (any number XORed with itself is 0)
- `x ^ 0 = x` (any number XORed with 0 is itself)
- XOR is commutative and associative

```
  1010
^ 1100
------
  0110   ← bits that differ
```

**Toggle bit i**: `n ^ (1 << i)`
**Find unique element**: XOR all elements — duplicates cancel out, leaving the unique one

### NOT (`~`) — Flip All Bits

`~n = -(n + 1)` in two's complement (JS 32-bit integers).

```
~5  = ~(00...00101) = (11...11010) = -6
~0  = -1
~-1 = 0
```

### Left Shift (`<<`) — Multiply by 2

`n << k` shifts bits left by k positions, equivalent to `n * 2^k`.

```
5 << 1 = 10   (5 * 2)
5 << 3 = 40   (5 * 8)
1 << k = 2^k  (power of 2)
```

### Right Shift (`>>`) — Divide by 2

`n >> k` shifts bits right by k positions, equivalent to `Math.floor(n / 2^k)`.

```
20 >> 1 = 10  (20 / 2)
20 >> 2 = 5   (20 / 4)
```

Note: `>>` is arithmetic (preserves sign bit). `>>>` is logical (fills with 0). Use `>>>` for unsigned operations.

---

## Essential Tricks

### Check if n is a Power of 2

A power of 2 has exactly one bit set: `0001`, `0010`, `0100`, `1000`, ...
Subtracting 1 flips all bits from the rightmost set bit down: `0100 - 1 = 0011`
AND of these two is always 0 for powers of 2.

```typescript
function isPowerOfTwo(n: number): boolean {
  return n > 0 && (n & (n - 1)) === 0;
}

// isPowerOfTwo(16) => true  (10000 & 01111 = 0)
// isPowerOfTwo(18) => false (10010 & 10001 = 10000 ≠ 0)
// isPowerOfTwo(0)  => false (edge case: 0 is not a power of 2)
```

---

### Get, Set, and Clear a Bit at Position i

```typescript
// Get bit i (returns 0 or 1)
function getBit(n: number, i: number): number {
  return (n >> i) & 1;
}

// Set bit i to 1
function setBit(n: number, i: number): number {
  return n | (1 << i);
}

// Clear bit i to 0
function clearBit(n: number, i: number): number {
  return n & ~(1 << i);
}

// Toggle bit i
function toggleBit(n: number, i: number): number {
  return n ^ (1 << i);
}

// Examples (using 8-bit representation for clarity):
// n = 0b01010110 = 86
// getBit(86, 2)   => 1  (bit 2 is set)
// setBit(86, 0)   => 87  (0b01010111)
// clearBit(86, 2) => 82  (0b01010010)
// toggleBit(86, 3) => 94 (0b01011110)
```

---

### Count Set Bits (Popcount) — Brian Kernighan's Algorithm

The trick: `n & (n - 1)` removes the **lowest set bit** of n.

```
n     = 1100  (12)
n - 1 = 1011  (11)
n & (n-1) = 1000  ← lowest set bit removed
```

Repeat until n becomes 0 — the number of iterations equals the number of set bits.

```typescript
function countSetBits(n: number): number {
  let count = 0;
  while (n !== 0) {
    n = n & (n - 1); // remove lowest set bit
    count++;
  }
  return count;
}

// countSetBits(7)  => 3  (111)
// countSetBits(8)  => 1  (1000)
// countSetBits(13) => 3  (1101)
// countSetBits(0)  => 0
```

**Time complexity**: O(k) where k = number of set bits, not O(32). Much faster than checking each bit individually when the number is sparse.

---

### XOR to Find Single Number

Every element appears twice except one. Find the unique element.

```typescript
function singleNumber(nums: number[]): number {
  let result = 0;
  for (const n of nums) {
    result ^= n; // pairs cancel: n ^ n = 0
  }
  return result; // only the unique element remains
}

// singleNumber([4,1,2,1,2]) => 4
// singleNumber([2,2,1])     => 1
// singleNumber([1])         => 1
```

**Why it works**: XOR is commutative and associative. All duplicates cancel to 0, leaving only the element that appeared an odd number of times. O(n) time, O(1) space — impossible to beat with a comparison-based approach.

---

### XOR to Find Missing Number (1 to n)

Given an array containing n distinct numbers taken from 0 to n (with one missing), find the missing one.

```typescript
function missingNumber(nums: number[]): number {
  let xor = nums.length; // start with n

  for (let i = 0; i < nums.length; i++) {
    xor ^= i ^ nums[i]; // XOR index and value
  }

  return xor;
  // Each index 0..n-1 is XORed once with itself (from both i and nums[i] if present)
  // The missing number is XORed with its index but has no corresponding nums[i] to cancel
}

// missingNumber([3,0,1]) => 2
// missingNumber([9,6,4,2,3,5,7,0,1]) => 8
// missingNumber([0]) => 1
```

**Alternative approach**: `expectedSum - actualSum = missing`, but XOR avoids potential integer overflow (though JS numbers handle this fine).

---

## More Useful Patterns

```typescript
// Check if n is even
const isEven = (n: number) => (n & 1) === 0;

// Check if n is odd
const isOdd = (n: number) => (n & 1) === 1;

// Multiply by 2
const times2 = (n: number) => n << 1;

// Integer division by 2 (floor)
const divBy2 = (n: number) => n >> 1;

// Swap two variables without a temp (XOR swap)
function xorSwap(a: number, b: number): [number, number] {
  a ^= b;
  b ^= a; // b = original a
  a ^= b; // a = original b
  return [a, b];
}

// Lowest set bit (isolate it)
const lowestSetBit = (n: number) => n & (-n);
// e.g. n=12 (1100): -n=...0100, n & -n = 0100 = 4 (the lowest set bit)

// Clear all bits from i to 0 (inclusive)
const clearBitsLow = (n: number, i: number) => n & (-1 << (i + 1));

// Clear all bits from MSB to i (inclusive)
const clearBitsHigh = (n: number, i: number) => n & ((1 << i) - 1);
```

---

## Common Interview Problems

| Problem | Key Trick | Complexity |
|---|---|---|
| Single number (one unique) | XOR all elements | O(n) time, O(1) space |
| Missing number | XOR indices and values | O(n) time, O(1) space |
| Power of two | `n & (n-1) === 0` | O(1) |
| Count set bits | Brian Kernighan: `n & (n-1)` | O(k) |
| Reverse bits | Shift and OR, 32 iterations | O(1) |
| Hamming distance | XOR then popcount | O(1) |
| Sum of two integers without `+` | XOR (sum without carry) + AND shifted (carry) | O(1) |

---

## Add Two Integers Without `+` (Bonus Deep Dive)

Classic bit manipulation interview question.

```typescript
function getSum(a: number, b: number): number {
  while (b !== 0) {
    const carry = (a & b) << 1; // AND gives carry bits, shift left to add in next position
    a = a ^ b;                   // XOR gives sum without carry
    b = carry;
  }
  return a;
}

// getSum(1, 2) => 3
// getSum(-1, 1) => 0
```

**Explanation**:
- `a ^ b` = sum of bits where exactly one is 1 (no carry)
- `(a & b) << 1` = carry bits shifted to the position where they should be added
- Repeat until no carry remains

---

## JavaScript/TypeScript Gotchas

- Bitwise operators convert operands to **32-bit signed integers** and return a 32-bit signed integer
- `~0 = -1`, `~-1 = 0` (two's complement)
- Right shift `>>` is arithmetic (sign-extends), `>>>` is logical (zero-fills) — use `>>>` for unsigned behavior
- Numbers larger than 2^31 - 1 lose precision with bitwise ops; use `BigInt` if needed
- `1 << 31` gives `-2147483648` (negative) due to sign bit in 32-bit representation

```typescript
// Safe pattern for 32-bit operations on JS numbers:
const bit = (n: number, i: number) => (n >>> i) & 1; // use >>> for unsigned shift
```

---

## Multi-Language Reference — XOR Single Number + Count Set Bits

> [!example]- JavaScript
> ```javascript
> // JavaScript
> function singleNumber(nums) {
>   return nums.reduce((acc, n) => acc ^ n, 0);
> }
> function countSetBits(n) {
>   let count = 0;
>   while (n) { n &= n - 1; count++; }
>   return count;
> }
> ```

> [!example]- Java
> ```java
> // Java
> public static int singleNumber(int[] nums) {
>     int result = 0;
>     for (int n : nums) result ^= n;
>     return result;
> }
> public static int countSetBits(int n) {
>     int count = 0;
>     while (n != 0) { n &= n - 1; count++; }
>     return count;
> }
> // Built-in: Integer.bitCount(n)  — counts set bits
> ```

> [!example]- Python
> ```python
> # Python
> def single_number(nums):
>     result = 0
>     for n in nums: result ^= n
>     return result
>
> def count_set_bits(n):
>     count = 0
>     while n:
>         n &= n - 1
>         count += 1
>     return count
> # Built-in: bin(n).count('1')  or  n.bit_count() (Python 3.10+)
> ```

> [!example]- C
> ```c
> // C
> int singleNumber(int nums[], int n) {
>     int result = 0;
>     for (int i = 0; i < n; i++) result ^= nums[i];
>     return result;
> }
> int countSetBits(unsigned int n) {
>     int count = 0;
>     while (n) { n &= n - 1; count++; }
>     return count;
> }
> // Built-in: __builtin_popcount(n)  (GCC extension)
> ```

> [!example]- C++
> ```cpp
> // C++
> int singleNumber(vector<int>& nums) {
>     int result = 0;
>     for (int n : nums) result ^= n;
>     return result;
> }
> int countSetBits(int n) {
>     return __builtin_popcount(n); // GCC intrinsic, O(1)
> }
> // Also: std::bitset<32>(n).count()
> ```

## Practice & Resources

**LeetCode — Essential Problems**
- [136 · Single Number](https://leetcode.com/problems/single-number/) — Easy · XOR all elements
- [191 · Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) — Easy · count set bits
- [190 · Reverse Bits](https://leetcode.com/problems/reverse-bits/) — Easy · shift and mask
- [268 · Missing Number](https://leetcode.com/problems/missing-number/) — Easy · XOR 0..n with array
- [338 · Counting Bits](https://leetcode.com/problems/counting-bits/) — Easy · DP with bit trick
- [371 · Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) — Medium · add without `+`

**References**
- [NeetCode · Bit Manipulation playlist](https://neetcode.io/roadmap)
- [Bit Twiddling Hacks](https://graphics.stanford.edu/~seander/bithacks.html) — classic reference for clever tricks

## Related

- [[Arrays & Strings]]
- [[Dynamic Programming]]
