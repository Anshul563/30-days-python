top_number = 50
bottom_number = 0

try:
    # We attempt the risky math here
    result = top_number / bottom_number
    print(f"The answer is {result}")

except ZeroDivisionError:
    # This runs only if the math fails due to division by zero
    print("Cannot divide by zero")