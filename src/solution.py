def calculate_factorial(n):
    def factorial(acc,k):
        if k == 0:
            return acc
        else:
            return factorial(acc*k, k-1)
        
    if n < 0:
        raise ValueError("Negative numbers are undefined for factorials.")
    else:
        return factorial(1,n)
    
    #testing
try:
    n = int(input("Enter an Integer that is not negative."))
    result = calculate_factorial(n)
    print(f"The factorial of {n} is {result}")
except ValueError as e:
    print(e)
    
