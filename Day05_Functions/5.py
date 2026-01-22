# Helper function: Does one small, specific task
def square(n):
    return n * n

# Main function: Uses the helper function
def sum_of_squares(a, b):
    # Calls square() twice
    sq_a = square(a) 
    sq_b = square(b)
    return sq_a + sq_b

# Usage
result = sum_of_squares(3, 4)
print(f"Result: {result}") 
# Logic: (3*3) + (4*4) = 9 + 16 = 25