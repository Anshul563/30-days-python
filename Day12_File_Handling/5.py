# Create a dummy source file first for this example
with open("note.txt", "w") as f:
    f.write("This is the original data.")

# --- The Copy Process ---
with open("note.txt", "r") as f_in, open("backup.txt", "w") as f_out:
    # 1. Read from the first file
    content = f_in.read()
    
    # 2. Write to the second file
    f_out.write(content)

print("Copy created successfully!")