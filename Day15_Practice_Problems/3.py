def check_armstrong(num):
    """
    Checks if a number is an Armstrong number.
    """
    # Convert number to string to count digits
    num_str = str(num)
    n = len(num_str)
    
    # Calculate sum of digits raised to the power of n
    sum_val = 0
    for digit in num_str:
        sum_val += int(digit) ** n
        
    # Check if sum equals original number
    if sum_val == num:
        return True
    else:
        return False

# Test cases
number = 153
if check_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")