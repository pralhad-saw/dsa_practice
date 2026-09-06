def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Pythonic variable swapping and modulo
    return a
#  (\(O(\log(\min(a, b)))\) 
# Example usage
num1 = 60
num2 = 48
print(f"The GCD is: {find_gcd(num1, num2)}")
# Output: The GCD is: 12


#  Using the Euclidean Algorithm (Loops)
