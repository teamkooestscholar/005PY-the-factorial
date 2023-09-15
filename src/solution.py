def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return "1"
    #Put the factor number in a array
    factors = []
    result = 1
    for i in range(1, n + 1):
        result *= i
        factors.append(str(i))

    #using slicing notation creates new list  but its in reverse
    factors = factors[::-1]
    factorial_expression = f"The factorial of {n} is {' x '.join(factors)} = {result}"
    return factorial_expression


number = int(input("Enter a number to give factorial: "))
result = factorial(number)
print(result)
