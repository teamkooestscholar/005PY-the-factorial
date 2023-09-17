def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result