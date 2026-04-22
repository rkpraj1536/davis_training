# Question 12: Custom Sorting Engine

students = [("Aman", 85, 20), ("Riya", 90, 18), ("Karan", 90, 19)]

for i in range(len(students)):
    for j in range(i + 1, len(students)):
        if students[i][1] < students[j][1] or (
            students[i][1] == students[j][1] and students[i][2] > students[j][2]
        ):
            students[i], students[j] = students[j], students[i]

print(students)
