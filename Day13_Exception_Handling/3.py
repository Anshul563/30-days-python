try:
    # Attempt to open the file
    file = open("note.txt", "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    # This runs if the computer cannot find the file
    print("File not found!")

finally:
    # This runs NO MATTER WHAT (success or failure)
    print("Execution completed.")