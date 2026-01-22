def factorial_iterative(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiply result by current number
    return result

# Usage
print(factorial_iterative(5))  # Output: 120