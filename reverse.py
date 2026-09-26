
num = int(input("Enter a number: "))


reverse = 0
temp = abs(num)

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num < 0:
    reverse = -reverse

print("Reversed number:", reverse)
