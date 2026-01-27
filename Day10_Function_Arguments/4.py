def add_everything(*args):
    # Python packs the inputs into a tuple named 'args'
    # Example: args might be (5, 10, 15)
    
    total = 0
    for number in args:
        total += number
    
    print(f"Input: {args}")
    print(f"Total: {total}\n")

# --- USAGE 1: Three arguments ---
add_everything(5, 10, 15)
# Output:
# Input: (5, 10, 15)
# Total: 30

# --- USAGE 2: Five arguments ---
add_everything(1, 1, 1, 1, 1)
# Output:
# Input: (1, 1, 1, 1, 1)
# Total: 5