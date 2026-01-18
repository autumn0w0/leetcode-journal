## Approach

This problem is solved using **Dynamic Programming**, following a pattern similar to the **Fibonacci sequence**.

### Idea

To reach step `n`, you can:
- Take **1 step** from `n - 1`
- Take **2 steps** from `n - 2`

So, the total number of ways to reach step `n` is the sum of the ways to reach the previous two steps.

### Explanation

- Define `dp[i]` as the number of ways to reach step `i`.
- Base cases:
  - `dp[0] = 1`
  - `dp[1] = 1`
- Transition:
    dp[i] = dp[i - 1] + dp[i - 2]
- Compute values iteratively up to `n`.

### Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

## Submission

https://leetcode.com/problems/climbing-stairs/submissions/1287808200/
