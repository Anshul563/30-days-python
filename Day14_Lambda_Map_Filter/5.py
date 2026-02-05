numbers = [1, 2, 3, 4, 5, 6]

# Step 1 (Inside): Filter keeps [2, 4, 6]
# Step 2 (Outside): Map squares them to [4, 16, 36]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

print(result)
# Output: [4, 16, 36]