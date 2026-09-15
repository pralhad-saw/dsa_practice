
def is_armstrong(number: int) -> bool:
    """
    An Armstrong number equals the sum of its digits,
    each raised to the power of the number of digits.
    Example: 153 = 1³ + 5³ + 3³
    """
    if number < 0:
        return False

    digits = str(number)
    power = len(digits)

    return sum(int(digit) ** power for digit in digits) == number

# Armstrong number
print(is_armstrong(153))       # True
print(is_armstrong(9474))      # True
print(is_armstrong(123))       # False
