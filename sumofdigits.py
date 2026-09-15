
def sum_of_digits(number: int) -> int:
    """
    Returns the sum of the digits of a number.
    """
    return sum(int(digit) for digit in str(abs(number)))

# Sum of digits
print(sum_of_digits(12345))    # 15
print(sum_of_digits(-987))     # 24


# #| Problem               | Time complexity              | Space complexity |
# | --------------------- | ---------------------------- | ---------------- |
# | Armstrong number      | O(d)O(d)O(d)                 | O(d)O(d)O(d)     |
# | Perfect number        | O(n)O(\\sqrt{n})O(n​)        | O(1)O(1)O(1)     |
# | Anagram               | O(nlog⁡n)O(n \\log n)O(nlogn) | O(n)O(n)O(n)     |
# | Vowels and consonants | O(n)O(n)O(n)                 | O(1)O(1)O(1)     |
# | Sum of digits         | O(d)O(d)O(d)                 | O(d)O(d)O(d)     |

