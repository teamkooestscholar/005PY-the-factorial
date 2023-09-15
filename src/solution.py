def calculate_factorial(n):
    if n < 0:
        return "The Given Value Appears To Be A Negative Value, Therefore It Cannot Be Computed."
    elif n == 0:
        return "0! = 1"
    else:
        output = 1
        #The Entirety Of The Function Computation
        factorials_Values = []
        for i in range(1, n + 1):
            output *= i
            factorials_Values.append(f"{i}")
            #To Reverse It As to Not Have The Output 1x2x3 but instead 3x2x1
            factorials_Values.reverse() 
            #Using the previous function in the other challenges .join for the purpose of showcasing the multiplied values for the given user input
        return f"Given Factorial of {n}! results for the output of {output} = {' x '.join(factorials_Values)}"

#User Input
#NOTE TO SELF! MAKE SURE THIS GOES BEFORE THE CODE BEFORE! OTHERWISE N = UNDEFINED!!
n = int(input("Insert Value For Factorial: "))

#This represents the process in determining if negative values where added as User Input Value
output = calculate_factorial(n)
if isinstance(output, str):
    print(output)
else:
    print(output)

