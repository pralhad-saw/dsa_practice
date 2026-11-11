"""
Next 7th challenge: Valid Palindrome II
This is a little harder and tests your ability to modify the two-pointer pattern.

Given a string, determine whether it can become a palindrome by deleting at most one character.

Examples:
Input	Output	Reason
"aba"	True	Already palindrome
"abca"	True	Delete c
"abc"	False	One deletion isn't enough

Try solving it independently. Don't rush. Think about what should happen when s[left] != s[right].
"""

def validPalindrome(s):

    def check(left, right):
      left, right = 0, len(s) - 1
      while left < right:
        if s[left] != s[right]:
          return False
        left+=1
        right-=1
      return True

        # Normal palindrome checking

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return check(left,right-1) or check(left-1, right)

        left += 1
        right -= 1

    return True
