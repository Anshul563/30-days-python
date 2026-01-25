def count_vowels(text):
    vowels = "aeiouAEIOU"  # Includes uppercase and lowercase
    count = 0

    for char in text:
        if char in vowels:
            count += 1
            
    return count

print(count_vowels("Hello World"))  # Output: 3 (e, o, o)