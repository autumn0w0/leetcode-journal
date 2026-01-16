# Add Two Numbers — Iterative Linked List Approach

## 🧠 Approach Explanation

This solution simulates **manual addition** of two numbers represented as linked lists. Since the digits are stored in **reverse order**, addition can be performed directly from the head of both lists.

A **carry variable** is used to handle cases where the sum of digits exceeds `9`.

---

## 🔍 How the Approach Works

- A **dummy node** is used to simplify linked list construction
- A pointer `cur` keeps track of the current node in the result list
- A variable `carry` stores any overflow during addition

The loop continues as long as:
- At least one list still has nodes left, or
- There is a remaining carry

---

## 🛠 Step-by-Step Breakdown

1. Initialize a dummy node and set `cur` to it
2. Initialize `carry` as `0`
3. While `l1`, `l2`, or `carry` exists:
   - If `l1` is not null, add its value to `carry` and move to the next node
   - If `l2` is not null, add its value to `carry` and move to the next node
4. Create a new node with value `carry % 10` and attach it to the result list
5. Update `carry` using integer division (`carry //= 10`)
6. Move the `cur` pointer forward
7. After the loop ends, return `dummy.next` as the head of the result list

---

## ⏱ Time & Space Complexity

- **Time Complexity:** `O(max(n, m))`  
  Where `n` and `m` are the lengths of the two linked lists

- **Space Complexity:** `O(max(n, m))`  
  Space used for the output linked list

---


## 🔗 My LeetCode Submission

[View my submission on LeetCode](https://leetcode.com/problems/add-two-numbers/submissions/1286657441/)