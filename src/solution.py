def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return "1 (0!)"
    else:
        factorial = 1
        factorial_steps = []
        
        # Calculate the factorial and keep track of the steps.
        for i in range(1, n + 1):
            factorial *= i
            factorial_steps.append(str(i))
        
        # Create an explanation of the calculation steps.
        steps = ' x '.join(factorial_steps)
        explanation = f"Explanation: {steps}"
        
        # Create the final result.
        result = f"Result: {factorial}"
        return explanation + "\n" + result

# Allow the user to input non-negative integers to calculate their factorial.
while True:
    user_input = input("Enter a non-negative integer to calculate its factorial (or 'q' to quit): ").strip().lower()
    
    # Check if the user wants to quit.
    if user_input == 'q':
        print("Exiting the factorial calculator.")
        break
    
    try:
        n = int(user_input)
        result = calculate_factorial(n)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a non-negative integer or 'q' to quit.")