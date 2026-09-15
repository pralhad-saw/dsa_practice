
# Detailed explanation about coomplexity I have given inc omment after code....

def are_anagrams(first: str, second: str) -> bool:
    """
    Checks whether two strings contain the same characters
    with the same frequencies.
    Spaces, punctuation, and case are ignored.
    """
    first_clean = sorted(
        character.lower()
        for character in first
        if character.isalnum()
    )

    second_clean = sorted(
        character.lower()
        for character in second
        if character.isalnum()
    )

    return first_clean == second_clean


# Anagram
print(are_anagrams("listen", "silent"))       # True
print(are_anagrams("Dormitory", "Dirty room"))  # True
print(are_anagrams("hello", "world"))          # False


# Anagram Check: Time and Space Complexity
# An anagram is a word or phrase formed by rearranging the characters of another word or phrase.

# For example:

# text
# listen → silent
# Both strings contain the same characters with the same frequencies, so they are anagrams.

# Sorting-based approach
# python
# def are_anagrams(first: str, second: str) -> bool:
#     first_clean = sorted(
#         character.lower()
#         for character in first
#         if character.isalnum()
#     )

#     second_clean = sorted(
#         character.lower()
#         for character in second
#         if character.isalnum()
#     )

#     return first_clean == second_clean
# How it works
# The function performs these steps:

# Converts each character to lowercase.

# Removes spaces and punctuation using isalnum().

# Sorts the characters in both strings.

# Compares the sorted results.

# Example:

# text
# "listen" → ['e', 'i', 'l', 'n', 's', 't']
# "silent" → ['e', 'i', 'l', 'n', 's', 't']
# Because the sorted character lists are equal, the strings are anagrams.

# Time complexity
# Let:

# 𝑛
# n be the length of the first string.

# 𝑚
# m be the length of the second string.

# Cleaning the strings
# The function examines every character once.

# python
# character.lower()
# character.isalnum()
# For the first string, this takes 
# 𝑂
# (
# 𝑛
# )
# O(n).

# For the second string, this takes 
# 𝑂
# (
# 𝑚
# )
# O(m).

# Therefore:

# 𝑂
# (
# 𝑛
# +
# 𝑚
# )
# O(n+m)
# Sorting the strings
# After cleaning, the characters are sorted.

# Sorting 
# 𝑛
# n characters takes:

# 𝑂
# (
# 𝑛
# log
# ⁡
# 𝑛
# )
# O(nlogn)
# Sorting 
# 𝑚
# m characters takes:

# 𝑂
# (
# 𝑚
# log
# ⁡
# 𝑚
# )
# O(mlogm)
# Comparing the strings
# The final comparison checks the characters one by one. In the worst case, it takes:

# 𝑂
# (
# min
# ⁡
# (
# 𝑛
# ,
# 𝑚
# )
# )
# O(min(n,m))
# This is at most 
# 𝑂
# (
# 𝑛
# +
# 𝑚
# )
# O(n+m), so it does not dominate the sorting operation.

# Overall time complexity
# Combining all operations:

# 𝑂
# (
# 𝑛
# +
# 𝑚
# )
# +
# 𝑂
# (
# 𝑛
# log
# ⁡
# 𝑛
# )
# +
# 𝑂
# (
# 𝑚
# log
# ⁡
# 𝑚
# )
# O(n+m)+O(nlogn)+O(mlogm)
# The sorting operations dominate the linear operations. Therefore, the overall time complexity is:

# 𝑂
# (
# 𝑛
# log
# ⁡
# 𝑛
# +
# 𝑚
# log
# ⁡
# 𝑚
# )
# O(nlogn+mlogm)
# ​
 
# If both strings have approximately the same length, where 
# 𝑛
# ≈
# 𝑚
# n≈m, this becomes:

# 𝑂
# (
# 𝑛
# log
# ⁡
# 𝑛
# )
# O(nlogn)
# ​
 
# Space complexity
# The sorted() function creates a new list of characters for each string.

# The first sorted list requires 
# 𝑂
# (
# 𝑛
# )
# O(n) space.

# The second sorted list requires 
# 𝑂
# (
# 𝑚
# )
# O(m) space.

# Therefore, the total auxiliary space complexity is:

# 𝑂
# (
# 𝑛
# +
# 𝑚
# )
# O(n+m)
# ​
 
# For two strings of approximately equal length:

# 𝑂
# (
# 𝑛
# )
# O(n)
# ​
 
# Python’s sorting algorithm uses additional temporary memory as well, but the sorted output lists already require linear space.

# Optimized frequency-counting approach
# Sorting is not required to check whether two strings are anagrams. We can count the frequency of each character instead.

# python
# from collections import Counter


# def are_anagrams(first: str, second: str) -> bool:
#     first_clean = (
#         character.lower()
#         for character in first
#         if character.isalnum()
#     )

#     second_clean = (
#         character.lower()
#         for character in second
#         if character.isalnum()
#     )

#     return Counter(first_clean) == Counter(second_clean)
# Complexity of the optimized approach
# The function processes each character once.

# Building the character count for the first string takes 
# 𝑂
# (
# 𝑛
# )
# O(n).

# Building the character count for the second string takes 
# 𝑂
# (
# 𝑚
# )
# O(m).

# Comparing the frequency dictionaries takes 
# 𝑂
# (
# 𝑘
# )
# O(k), where 
# 𝑘
# k is the number of unique characters.

# Since 
# 𝑘
# k is no greater than 
# 𝑛
# +
# 𝑚
# n+m, the overall time complexity is:

# 𝑂
# (
# 𝑛
# +
# 𝑚
# )
# O(n+m)
# ​
 
# The frequency dictionary stores each unique character. If 
# 𝑘
# k represents the number of unique characters, the space complexity is:

# 𝑂
# (
# 𝑘
# )
# O(k)
# ​
 
# In the general case, 
# 𝑘
# k can be as large as 
# 𝑛
# +
# 𝑚
# n+m, so the worst-case space complexity is:

# 𝑂
# (
# 𝑛
# +
# 𝑚
# )
# O(n+m)
# ​
 
# For a fixed character set, such as lowercase English letters, 
# 𝑘
# k is limited to 26. In that case, the auxiliary space can be considered:

# 𝑂
# (
# 1
# )
# O(1)
# ​
 
# The frequency-counting approach is usually more efficient because it avoids sorting and runs in linear time on average. Dictionary lookups and updates are expected 
# 𝑂
# (
# 1
# )
# O(1) operations, while Python sorting is generally 
# 𝑂
# (
# 𝑛
# log
# ⁡
# 𝑛
# )
# O(nlogn).

# Complexity comparison
# Approach	Time complexity	Space complexity
# Sorting-based	
# 𝑂
# (
# 𝑛
# log
# ⁡
# 𝑛
# +
# 𝑚
# log
# ⁡
# 𝑚
# )
# O(nlogn+mlogm)	
# 𝑂
# (
# 𝑛
# +
# 𝑚
# )
# O(n+m)
# Frequency-counting	
# 𝑂
# (
# 𝑛
# +
# 𝑚
# )
# O(n+m) average	
# 𝑂
# (
# 𝑘
# )
# O(k)
# Frequency-counting with fixed alphabet	
# 𝑂
# (
# 𝑛
# +
# 𝑚
# )
# O(n+m)	
# 𝑂
# (
# 1
# )
# O(1)
# Recommended implementation
# For optimal performance, use frequency counting:

# python
# from collections import Counter


# def are_anagrams(first: str, second: str) -> bool:
#     first_clean = (
#         character.lower()
#         for character in first
#         if character.isalnum()
#     )

#     second_clean = (
#         character.lower()
#         for character in second
#         if character.isalnum()
#     )

#     return Counter(first_clean) == Counter(second_clean)
# Example:

# python
# print(are_anagrams("listen", "silent"))
# # True

# print(are_anagrams("Dormitory", "Dirty room"))
# # True

# print(are_anagrams("hello", "world"))
# # False
# README-ready conclusion
# The sorting-based anagram solution has a time complexity of 
# 𝑂
# (
# 𝑛
# log
# ⁡
# 𝑛
# +
# 𝑚
# log
# ⁡
# 𝑚
# )
# O(nlogn+mlogm), because both strings must be sorted. Its space complexity is 
# 𝑂
# (
# 𝑛
# +
# 𝑚
# )
# O(n+m) because sorted character lists are created. A more efficient solution uses character-frequency counting, which processes both strings in one pass and has an average time complexity of 
# 𝑂
# (
# 𝑛
# +
# 𝑚
# )
# O(n+m). The frequency-counting approach is preferred when performance is important.
