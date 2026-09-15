


def is_perfect(number: int) -> bool:
    """
    A perfect number equals the sum of its proper divisors.
    Example: 6 = 1 + 2 + 3
    """
    if number <= 1:
        return False

    divisor_sum = 1
    divisor = 2

    # Check only up to the square root for efficiency
    while divisor * divisor <= number:
        if number % divisor == 0:
            divisor_sum += divisor

            paired_divisor = number // divisor
            if paired_divisor != divisor:
                divisor_sum += paired_divisor

        divisor += 1

    return divisor_sum == number



# Perfect number
print(is_perfect(6))           # True
print(is_perfect(28))          # True
print(is_perfect(12))          # False
