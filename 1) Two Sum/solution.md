# Two Sum — Brute Force Approach

## 🧠 Approach Explanation

This solution uses a **brute force** technique to check all possible pairs of numbers in the array to find two values whose sum equals the target.

Instead of optimizing early, the idea here is to focus on **correctness and simplicity**.

---

## 🔍 How the Approach Works

- We use **two nested loops** to generate every unique pair `(i, j)` such that:
  - `i < j`
  - The same element is never used twice

- For each pair:
  - We check whether `nums[i] + nums[j] == target`
  - As soon as a valid pair is found, we return their indices

Because the problem guarantees **exactly one valid answer**, we can safely return immediately.

---

## 🛠 Step-by-Step Breakdown

1. The outer loop fixes the first index `i`
2. The inner loop checks all indices `j` that come **after** `i`
3. For each pair `(i, j)`:
   - Calculate the sum of `nums[i]` and `nums[j]`
   - Compare it with the target
4. If the sum matches the target, return `[i, j]`

This ensures:
- No duplicate pairs
- No reuse of the same element

---

## ⏱ Time & Space Complexity

- **Time Complexity:** `O(n²)`  
  Every element is compared with every other element

- **Space Complexity:** `O(1)`  
  No extra data structures are used

---

## 🔗 My LeetCode Submission

[View my submission on LeetCode](https://leetcode.com/problems/two-sum/submissions/1285796048/)
