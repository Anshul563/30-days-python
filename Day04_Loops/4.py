N = int(input("Enter a number N:"))

total_sum = 0
for i in range(1, N + 1):
    total_sum += i
print(f"The sum of all numbers from 1 to {N} is {total_sum}.")