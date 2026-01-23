numbers = [10, 25, 3, 42, 7]

maximum = max(numbers)
minimum = min(numbers)

print("Maximum number is:", maximum)
print("Minimum number is:", minimum)


# using Loops
numbers = [10, 25, 3, 42, 7]

max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Maximum number is:", max_num)
print("Minimum number is:", min_num)
