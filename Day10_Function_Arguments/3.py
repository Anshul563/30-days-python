# We assign "Medium" to the 'size' parameter in the definition
def make_coffee(coffee_type, size="Medium"):
    print(f"Making a {size} {coffee_type}.")

# --- USAGE 1: Using the Default ---
# We only provide the coffee_type. 
# Python sees 'size' is missing and automatically uses "Medium".
make_coffee("Latte")
# Output: Making a Medium Latte.


# --- USAGE 2: Overriding the Default ---
# We provide a second argument.
# This overrides "Medium" with "Large".
make_coffee("Cappuccino", "Large")
# Output: Making a Large Cappuccino.