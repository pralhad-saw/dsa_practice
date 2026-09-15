
def sum_of_digits(number: int) -> int:
    """
    Returns the sum of the digits of a number.
    """
    return sum(int(digit) for digit in str(abs(number)))

# Sum of digits
print(sum_of_digits(12345))    # 15
print(sum_of_digits(-987))     # 24
