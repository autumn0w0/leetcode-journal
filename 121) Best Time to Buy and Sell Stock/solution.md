## Approach

This problem is solved using a **Greedy approach** by tracking the **minimum price so far** and calculating the **maximum profit** at each step.

### Idea

To maximize profit:
- Buy at the **lowest price** seen so far
- Sell at the **current price** if it gives a better profit

We iterate through the array once and:
- Keep updating the minimum price
- Calculate potential profit at each step

### Explanation

- Initialize:
  - `minPrice = ∞` (to track the lowest buying price)
  - `maxProfit = 0` (to track the best profit)

- For each price:
  - If the current price is lower than `minPrice`, update `minPrice`
  - Else, calculate profit = `price - minPrice`
  - Update `maxProfit` if this profit is higher

### Code Logic

- `minPrice` stores the best buying opportunity
- `maxProfit` stores the best selling outcome
- We ensure buying always happens before selling

### Complexity

- **Time Complexity:** `O(n)` (single pass through the array)
- **Space Complexity:** `O(1)` (no extra space used)

## Submission

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1287829162/