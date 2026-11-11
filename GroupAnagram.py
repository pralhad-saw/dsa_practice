"""Day 1 – Problem 4: Group Anagrams
Medium · LeetCode 49
This is an important Google interview pattern.

Problem: Given an array of strings, group all anagrams together.

Example:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Expected output (group order doesn't matter):
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]

Hint
Remember your previous problem?

You counted character frequencies using a dictionary.

Now think:

If "eat", "tea" and "ate" have identical character frequencies, can we use those frequencies as a dictionary key?

Your challenge:

Decide how to generate a unique key for each anagram group.

Use a hash map.

Write the complete Python function.

Don't rush to see the solution. Try independently first."""


