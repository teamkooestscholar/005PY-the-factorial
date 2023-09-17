def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usages
result1 = calculate_factorial(5)
result2 = calculate_factorial(0)
result3 = calculate_factorial(-3)

print("Factorial of 5:", result1)  # This will print "Factorial of 5: 120"
print("Factorial of 0:", result2)  # This will print "Factorial of 0: 1"
print("Factorial of -3:", result3)  # This will print "Factorial is not defined for negative numbers"
