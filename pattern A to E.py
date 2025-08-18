# Python program to print the given pattern

n = 5  # number of rows (change if needed)

for i in range(n):
    # Left side letters (A to decreasing limit)
    for j in range(65, 65 + n - i):
        print(chr(j), end=" ")

    # Spaces in the middle
    for j in range(i * 2 - 1):
        print(" ", end=" ")

    # Right side letters (decreasing order)
    for j in range(65 + n - i - 1, 64, -1):
        print(chr(j), end=" ")

    print()
