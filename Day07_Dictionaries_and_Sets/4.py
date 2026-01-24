# A list with many duplicate numbers
raw_data = [10, 20, 10, 30, 20, 40, 10]

# 1. Convert the list to a set to remove duplicates
unique_set = set(raw_data)

print(unique_set)
# Output: {40, 10, 20, 30} 
# (Note: The order might look random because sets are unordered)

# 2. (Optional) Convert it back to a list if you need to index it later
unique_list = list(unique_set)

print(unique_list)
# Output: [40, 10, 20, 30]