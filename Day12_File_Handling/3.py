# Open 'notes.txt' in append mode
with open("note.txt", "a") as f:
    f.write("\nThis is an extra line.")
    f.write("\nAppending is useful for logs.")