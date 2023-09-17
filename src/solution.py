def calculate_factorial(n):
    if n < 0:
        return None  
    elif n == 0:
        return 1  
    else:
        return n * calculate_factorial(n - 1)
    
factorial5 = calculate_factorial(5)
factorial10 = calculate_factorial(10)

print("The factorial of 5 is: ", factorial5)
print("The factorial of 10 is: ", factorial10)