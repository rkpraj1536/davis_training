# 1. Student Grade Analyzer

def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid Marks"
    elif marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

for student_number in range(1, 6):
    marks = float(input(f"Enter marks of Student {student_number}: "))
    grade = calculate_grade(marks)
    print(f"Grade of Student {student_number}: {grade}")
