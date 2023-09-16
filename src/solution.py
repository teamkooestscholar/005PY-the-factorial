def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result

# Example usage:
n = 5
print(calculate_factorial(n))  # Output: 120
