def calculate_factorial(n):
    pass # Remove the function "pass" and write your code here
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)
