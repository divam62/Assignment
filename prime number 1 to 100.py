# Program to print prime numbers from 1 to 100

for num in range(2, 101):   # numbers from 2 to 100
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # check divisibility up to sqrt(num)
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
