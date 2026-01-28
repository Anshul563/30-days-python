# File: main.py
import formulas

# 1. Use a variable from the module
print(f"Current Tax Rate: {formulas.tax_rate}")

# 2. Use a function from the module
total = formulas.calculate_total(100)
print(f"Total with tax: ${total}")

# 3. Use another function
print(formulas.greet_user("Alice"))