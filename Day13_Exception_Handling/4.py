print("1. Opening database connection...")

try:
    # Attempt the calculation
    x = 10 / 0
    print("Calculation result:", x)

except ZeroDivisionError:
    # Handle the error
    print("Error: Calculation failed.")

finally:
    # This runs regardless of the error above
    print("3. Closing database connection...")