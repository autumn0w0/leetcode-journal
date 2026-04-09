## Approach

This problem is solved using **Bit Manipulation (XOR)**, which allows us to achieve **O(n)** time and **O(1)** space.

### Idea

The key observation is based on properties of the **XOR (^) operator**:

- `a ^ a = 0` (same numbers cancel out)
- `a ^ 0 = a`
- XOR is **commutative and associative**

So, if we XOR all elements:
- Pairs of identical numbers cancel out
- Only the **unique number remains**

### Explanation

- Initialize a variable `repeats = 0`
- Iterate through each number in the array:
  - Perform `repeats ^= i`
- Since duplicates cancel each other, the final value of `repeats` will be the single number

### Code Logic

- `repeats` acts as an accumulator for XOR operations
- Every duplicate number nullifies itself
- Only the number that appears once remains at the end

### Complexity

- **Time Complexity:** `O(n)` (single traversal of array)
- **Space Complexity:** `O(1)` (no extra space used)

## Submission

https://leetcode.com/problems/single-number/submissions/1287723541/