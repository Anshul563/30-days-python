user_input = "twenty"

try:
    # Attempt to convert the text to a number
    age = int(user_input)
    print(f"You are {age} years old.")

except ValueError:
    # This runs if the input is text that looks like a word, not a digit
    print("Please enter a valid number.")