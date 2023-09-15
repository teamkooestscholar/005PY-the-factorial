def calculate_factorial(n):
    return 1 if n <= 1 else n * calculate_factorial(n - 1)

result = calculate_factorial(0)
print(result)