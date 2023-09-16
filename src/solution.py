def calculate_factorial(n):
    pass # Remove the function "pass" and write your code here
from functools import reduce

def calculate_factorial(n):
    return reduce(lambda x, y: x * y, range (1, n + 1), 1)

n_input = input("Enter a number for factorial: ")
n_input = int(n_input)

answer = calculate_factorial(n_input)
print("The factorial of ", n_input,  "is: ", answer)
