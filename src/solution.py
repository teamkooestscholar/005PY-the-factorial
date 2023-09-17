def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

result1 = calculate_factorial(5)
print(f"Ans: {result1}")
print(f"The factorial of 5 is 5 x 4 x 3 x 2 x 1 = {result1}")
print()

result2 = calculate_factorial(10)
print(f"Ans: {result2}")
print(f"The factorial of 10 is 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = {result2}")
