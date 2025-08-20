def print_numbers(n):
    if n > 5:    # base condition to stop recursion
        return
    print(n)
    print_numbers(n + 1)   # recursive call

# call the function starting from 1
print_numbers(1)
