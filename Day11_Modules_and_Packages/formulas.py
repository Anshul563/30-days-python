# File: formulas.py

# A variable
tax_rate = 0.15

# A function
def calculate_total(price):
    """Calculates price including tax"""
    return price * (1 + tax_rate)

# A function
def greet_user(name):
    return f"Hello, {name}!"