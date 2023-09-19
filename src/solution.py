def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return "1 (0!)"
    else:
        factorial = 1
        factorial_steps = []
        for i in range(1, n + 1):
            factorial *= i
            factorial_steps.append(str(i))
        steps = ' x '.join(factorial_steps)
        explanation = f"Explanation: {steps}"
        result = f"Result: {factorial}"
        return explanation + "\n" + result

while True:
    user_input = input("Enter a non-negative integer to calculate its factorial (or 'q' to quit): ").strip().lower()
    if user_input == 'q':
        print("Exiting the factorial calculator.")
        break
    try:
        n = int(user_input)
        result = calculate_factorial(n)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a non-negative integer or 'q' to quit.")