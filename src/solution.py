from functools import reduce

def factorial(n):
    """ Return the factorial of a number """
    if n < 0:
        raise ValueError("Factorial is Only defined for non-negative integers")
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

user_num = int(input("Enter a number that you want to get its factorial value: "))
print(f"The factorial of {user_num} is {factorial(user_num)}")