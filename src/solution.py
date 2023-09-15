# Description: Write a function that calculates and returns the factorial of a non-negative integer.

# Example #1
# Input: `calculate_factorial(5)`
# Output: `120`
# Explanation: The factorial of 5 is 5 x 4 x 3 x 2 x 1 = 120.

# Example #2
# Input: `calculate_factorial(10)`
# Output: `3628800`
# Explanation: The factorial of 10 is 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 3628800.

# Constraints
# Do not use the built-in math.factorial() function.
# Do not use recursion.
# Do not use any loops.

from functools import reduce

def factorial(n):
    """ Return the factorial of a number """
    if n < 0:
        raise ValueError("Factorial is Only defined for non-negative integers")
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

user_num = int(input("Enter a number that you want to get its factorial value: "))
print(f"The factorial of {user_num} is {factorial(user_num)}")

