# EASY: 005 Python - Calculate the Factorial of a Number

## Description

Write a function that calculates and returns the factorial of a non-negative integer.

## Sample Solution

```python
def calculate_factorial(n):
    return n * calculate_factorial(n - 1)
```

## Examples

### Example 1

```markdown
Input: `calculate_factorial(5)`
Output: `120`
Explanation: The factorial of 5 is 5 x 4 x 3 x 2 x 1 = 120.
```

### Example 2

```markdown
Input: `calculate_factorial(10)`
Output: `3628800`
Explanation: The factorial of 10 is 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 3628800.
```

## Constraints

- Do not use the built-in `math.factorial()` function.
- Do not use recursion.
- Do not use any loops.

## Testing

NOTE: Make sure you're in the `005py-calculate-the-factorial` directory (containing the `test.py` file) when executing the command above.

- To navigate to the directory containing the test file from the current terminal, run the following command:

```bash
cd scr/
```

- Then run the following command in a terminal to test your code:

```bash
python -m unittest -v test
```

- And make sure you get the following output:

```bash
test_factorial_of_large_number (test.TestCalculateFactorial.test_factorial_of_large_number) ... ok
test_factorial_of_positive_number (test.TestCalculateFactorial.test_factorial_of_positive_number) ... ok
test_factorial_of_zero (test.TestCalculateFactorial.test_factorial_of_zero) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```
