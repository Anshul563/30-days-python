def sum_of_digits(n):
    """
    Calculates the sum of digits of a number mathematically.
    """
    total = 0
    # Handle negative numbers by converting to positive
    n = abs(n)
    
    while n > 0:
        digit = n % 10  # Get the last digit
        total += digit  # Add it to the sum
        n = n // 10     # Remove the last digit
        
    return total

# Test the function
number = 6789
result = sum_of_digits(number)
print(f"The sum of digits of {number} is: {result}")