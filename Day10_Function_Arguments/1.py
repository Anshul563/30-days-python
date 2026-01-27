def calculate_power(base, exponent):
    result = base ** exponent
    print(f"{base} to the power of {exponent} is: {result}")

# --- CORRECT USAGE ---
# We want 2 to the power of 3 (2^3)
# 1st argument (2) -> 1st parameter (base)
# 2nd argument (3) -> 2nd parameter (exponent)
calculate_power(2, 3)
# Output: 2 to the power of 3 is: 8


# --- INCORRECT USAGE (Swapped) ---
# If we swap the positions, the logic changes completely.
# 1st argument (3) -> 1st parameter (base)
# 2nd argument (2) -> 2nd parameter (exponent)
calculate_power(3, 2)
# Output: 3 to the power of 2 is: 9