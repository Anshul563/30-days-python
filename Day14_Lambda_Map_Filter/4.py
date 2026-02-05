from functools import reduce  # We must import this first

numbers = [1, 2, 3, 4]

# Use reduce to add x and y cumulatively
total_sum = reduce(lambda x, y: x + y, numbers)

print(total_sum)
# Output: 10