---
tags: [concept, data-structure, tech]
created: 2026-03-21
related: [Big O Notation, Arrays]
---

# Hash Tables

## What it is
A data structure that maps keys to values using a hash function. The key is transformed into an index, and the value is stored there. In JS/TS: `{}`, `Map`, `Set` are all hash-based.

## Complexity
| Operation | Average | Worst case |
|---|---|---|
| Get | O(1) | O(n) |
| Set | O(1) | O(n) |
| Delete | O(1) | O(n) |

Worst case happens when many keys hash to the same slot (collision) — rare with good hash functions.

## How it works
1. Take the key (e.g. `"name"`)
2. Run through a hash function → get an index (e.g. `42`)
3. Store the value at that index in an underlying array
4. Lookup: hash the key again → go directly to that index

**Collision handling:** two keys hash to same index → chaining (linked list at slot) or open addressing.

## How we use it
- Any time you need O(1) lookup by key
- Deduplication (use a Set)
- Counting frequencies
- Caching/memoization

```typescript
// Frequency count — classic hash table use case
function charFrequency(str: string): Map<string, number> {
  const freq = new Map<string, number>();
  for (const char of str) {
    freq.set(char, (freq.get(char) ?? 0) + 1);
  }
  return freq;
}

// Check if two strings are anagrams — O(n)
function isAnagram(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  const freq = charFrequency(a);
  for (const char of b) {
    if (!freq.get(char)) return false;
    freq.set(char, freq.get(char)! - 1);
  }
  return true;
}

// Object vs Map — prefer Map when:
// - keys are not strings (numbers, objects)
// - need to preserve insertion order reliably
// - frequently adding/removing keys
```

## Object vs Map vs Set
| | Object | Map | Set |
|---|---|---|---|
| Keys | strings/symbols only | any type | N/A (values only) |
| Order | not guaranteed (integers first) | insertion order | insertion order |
| Size | manual (`Object.keys().length`) | `.size` | `.size` |
| Use when | simple config/data | key-value with any key type | unique values / dedup |

## Multi-Language Reference — Hash Map / Set Operations

```javascript
// JavaScript
const map = new Map();
map.set('key', 1);
const val = map.get('key');     // 1
map.has('key');                  // true
map.delete('key');
// Set for unique values
const set = new Set([1, 2, 2, 3]); // {1, 2, 3}
set.add(4); set.has(2); set.delete(2);
// Object as hash map (string keys only):
const freq = {};
for (const c of 'hello') freq[c] = (freq[c] || 0) + 1;
```

```java
// Java
HashMap<String, Integer> map = new HashMap<>();
map.put("key", 1);
int val = map.getOrDefault("key", 0);
map.containsKey("key");
map.remove("key");
// Iterate:
for (Map.Entry<String, Integer> e : map.entrySet()) { e.getKey(); e.getValue(); }
// HashSet:
HashSet<Integer> set = new HashSet<>();
set.add(1); set.contains(1); set.remove(1);
```

```python
# Python — dict is a hash map
freq = {}
freq['key'] = freq.get('key', 0) + 1
'key' in freq         # True
del freq['key']
# defaultdict for cleaner counters:
from collections import defaultdict, Counter
freq = Counter("hello")  # {'l': 2, 'h': 1, 'e': 1, 'o': 1}
# Set:
s = {1, 2, 3}
s.add(4); 2 in s; s.discard(2)
```

```c
// C — no built-in hash map; use array-based frequency count for chars
int freq[256] = {0};
char* s = "hello";
for (int i = 0; s[i]; i++) freq[(unsigned char)s[i]]++;
// For general hash maps, use open addressing or chaining manually
// or use uthash library (common in competitive C)
```

```cpp
// C++
#include <unordered_map>
#include <unordered_set>
unordered_map<string, int> map;
map["key"] = 1;
map.count("key");      // 1 if exists, 0 otherwise
map.erase("key");
// Range-based iterate:
for (auto& [k, v] : map) { /* k, v */ }
// Set:
unordered_set<int> s;
s.insert(1); s.count(1); s.erase(1);
```

## Practice & Resources

**LeetCode — Essential Problems**
- [1 · Two Sum](https://leetcode.com/problems/two-sum/) — Easy · map value → index
- [242 · Valid Anagram](https://leetcode.com/problems/valid-anagram/) — Easy · character frequency count
- [49 · Group Anagrams](https://leetcode.com/problems/group-anagrams/) — Medium · sorted key → group
- [347 · Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) — Medium · frequency map + heap or bucket
- [128 · Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) — Medium · set lookup for O(n) solution
- [146 · LRU Cache](https://leetcode.com/problems/lru-cache/) — Medium · HashMap + doubly linked list

**References**
- [NeetCode · Arrays & Hashing playlist](https://neetcode.io/roadmap)
- [VisuAlgo · Hash Table](https://visualgo.net/en/hashtable) — animated open addressing and chaining

## Related
- [[Big O Notation]] — why O(1) average is powerful
- [[Arrays]] — hash tables use arrays internally
