import math

def is_prime(n):
    if n <= 1:
        return False
    
    limit = int(math.sqrt(n)) + 1
    
    for i in range(2, limit):
        if n % i == 0:
            return False  
            
    return True   

# Usage
number = 29
if is_prime(number):
    print(f"{number} is a Prime Number")
else:
    print(f"{number} is NOT a Prime Number")