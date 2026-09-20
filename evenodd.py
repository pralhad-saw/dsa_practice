
n = int(input("Enter the limit: "))

print("Even numbers:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")

print("\nOdd numbers:")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
