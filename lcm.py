
import math

def calculate_lcm(a, b):
    # ABS prevents issues with negative numbers
    return abs(a * b) // math.gcd(a, b)

print(calculate_lcm(12, 18))  # Output: 36


#method 2 using math.lcm()
