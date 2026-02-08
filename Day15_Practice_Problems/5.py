def is_palindrome(n):
    """
    Checks if a number is a palindrome mathematically.
    """
    # Negative numbers are not palindromes
    if n < 0:
        return False
        
    original_n = n
    reversed_n = 0
    
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n = n // 10
        
    return original_n == reversed_n

# Test cases
num = 12321
result = is_palindrome(num)
print(f"Is {num} a palindrome? {result}")