# method 1--- calculating using a maths formula to lcm
import math

def calculate_lcm(a, b):
    # ABS prevents issues with negative numbers
    return abs(a * b) // math.gcd(a, b)

print(calculate_lcm(12, 18))  # Output: 36


# #method 2 using math.lcm()

# Python 3.9+
# import math

# # For two numbers
# print(math.lcm(12, 18))  # Output: 36

# # For multiple numbers
# print(math.lcm(4, 6, 8))  # Output: 24
