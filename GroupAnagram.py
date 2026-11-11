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


"""my solution - no ai - no copy paste not even google for syntax
we can sort each item and use that sorted item as a key for dictonary and at last just return dictionary as a lists"""

def solution(strs):
    freq = {}
    for x in strs:
        y = tuple(sorted(x))
        if y not in freq:
            freq[y]= []
        freq[y].append(x)
    return list(freq.values())
    
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

"""
2. Complexity analysis
Let:
- n = number of strings
- k = maximum length of a string
Operation	Complexity
Sort each string	O(k log k)
Process all strings	O(n × k log k)
Dictionary grouping	O(n) average, excluding key construction

Overall:
- Time: O(n × k log k)
- Space: O(n × k) for storing grouped strings and keys.
"""
