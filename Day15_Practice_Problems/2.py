def factorial_recursive(n):
    """
    Calculates the factorial of n using recursion.
    """
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Check for negative input
    elif n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    # Recursive step
    else:
        return n * factorial_recursive(n - 1)

# Example usage: Calculate 5!
number = 5
try:
    result = factorial_recursive(number)
    print(f"Factorial of {number} is: {result}")
except ValueError as e:
    print(e)