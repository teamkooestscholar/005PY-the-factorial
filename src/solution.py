def calculate_factorial(n):
    if n < 0:
        raise ValueError("Negative numbers are undefined for factorials.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

try:
    n = int(input("Enter a non-negative integer: "))
    result = calculate_factorial(n)
    print(f"The factorial of {n} is {result}")
except ValueError as e:
    print(e)