marks1 = input("Enter marks for subject 1: ")
marks2 = input("Enter marks for subject 2: ")
marks3 = input("Enter marks for subject 3: ")

total_marks = int(marks1) + int(marks2) + int(marks3)

if total_marks >= 240:
    print("Grade: A")
elif total_marks >= 180:
    print("Grade: B")
elif total_marks >= 120:
    print("Grade: C")
else:
    print("Grade: D")