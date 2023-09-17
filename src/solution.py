import math

def calculate_factorial(n):
    if n < 0:
        return None  
    elif n == 0:
        return 1  
    else:
        return int(math.gamma(n + 1)) 

#Example1
result1 = calculate_factorial(5)
print("Input: 'calculate_factorial(5)'")
print("Output:", result1)  
print("Explanation: The factorial of 5 is 5 x 4 x 3 x 2 x 1 = ", result1)
#Example2
result2 = calculate_factorial(10)
print("\nInput: 'calculate_factorial(10)'")
print("Output:", result2) 
print("Explanation: The factorial of 10 is 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = ", result2)

