# 1. Union (|)
team_A = {"Alice", "Bob", "Charlie"}
team_B = {"Charlie", "David", "Edward"}

# Combine both teams
all_students = team_A | team_B 

print(all_students)
# Output: {'Alice', 'Bob', 'Charlie', 'David', 'Edward'}
# Note: "Charlie" appears only once, even though he was in both teams.