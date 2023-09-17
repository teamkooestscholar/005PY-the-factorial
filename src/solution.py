def calculate_factorial(n):
    if n < 0:
        raise ValueError("Negative numbers are undefined for factorials.")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result


