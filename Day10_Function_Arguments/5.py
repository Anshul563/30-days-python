def create_profile(name, **kwargs):
    # kwargs is a standard Python dictionary
    print(f"User: {name}")
    
    # We can loop through the dictionary using .items()
    for key, value in kwargs.items():
        print(f" - {key}: {value}")
    print("-" * 20)

# --- USAGE 1: Minimal Info ---
create_profile("Alice", age=25, city="New York")
# Output:
# User: Alice
#  - age: 25
#  - city: New York

# --- USAGE 2: Different Info ---
create_profile("Bob", job="Engineer", status="Active", level=5)
# Output:
# User: Bob
#  - job: Engineer
#  - status: Active
#  - level: 5