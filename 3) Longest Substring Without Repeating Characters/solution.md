## 🔍 Approach

This solution uses the **sliding window** technique to find the longest substring without repeating characters in **O(n)** time.

- A pointer `start` marks the beginning of the current substring.
- A dictionary `usedchar` stores the **latest index** at which each character appeared.
- As we iterate through the string:
  - If the current character has appeared before **and** its last occurrence is within the current window, move `start` to one position after that occurrence to avoid duplicates.
  - Otherwise, update the maximum length using the current window size.
- Continuously update the character’s latest index in the dictionary.

This ensures that the window always contains unique characters while scanning the string only once.
