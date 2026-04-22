# Question 20: Student Grouping System

students = [
    ("Aman", "A"),
    ("Riya", "B"),
    ("Karan", "A"),
    ("Sneha", "C")
]

groups = {}

for name, grade in students:
    if grade not in groups:
        groups[grade] = []

    groups[grade].append(name)

print(groups)
