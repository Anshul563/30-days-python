# Open the file in read mode
with open("note.txt", "r") as f:
    data = f.read()          # 1. Read the whole file into a string
    words = data.split()     # 2. Split string into a list of words
    count = len(words)       # 3. Count the number of items in the list

print("Total words:", count)