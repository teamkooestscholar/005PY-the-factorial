def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

try:
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        raise ValueError("Negative numbers are undefined for factorials.")
    result = calculate_factorial(n)
    print(f"The factorial of {n} is {result}")
except ValueError as e:
    print(e)