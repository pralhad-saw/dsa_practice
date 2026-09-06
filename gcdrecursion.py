#gcd is also called hcf
def find_gcd_recursive(a, b):
    if b == 0:
        return a
    return find_gcd_recursive(b, a % b)

# Example usage
num1 = 60
num2 = 48
print(f"The GCD is: {find_gcd_recursive(num1, num2)}")
# Output: The GCD is: 12
