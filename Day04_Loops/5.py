# Take input from the user
num = int(input("Enter a number: "))

reversed_num = 0

# Loop until the number becomes 0
while num > 0:
    digit = num % 10                # 1. Get the last digit
    reversed_num = reversed_num * 10 + digit  # 2. Append digit
    num = num // 10                 # 3. Remove last digit

print(f"Reversed Number: {reversed_num}")