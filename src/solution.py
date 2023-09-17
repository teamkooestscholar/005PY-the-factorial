def calculate_factorial(n):
    if n == 0:
        return 1

    result = 1
    while n > 0:
        result *= n
        n -= 1

    return result

print(calculate_factorial(5))  # Output: 120
print(calculate_factorial(10))  # Output: 3628800
