numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Use filter to keep items where the remainder is 0
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)
# Output: [2, 4, 6, 8]