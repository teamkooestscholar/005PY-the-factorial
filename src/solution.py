def calculate_factorial(n):
    if(n < 0):
        return "Error: n must be >= 0"
    elif(n == 0):
        return 1
    else:
        return n * calculate_factorial(n - 1)

calculate_factorial(5)