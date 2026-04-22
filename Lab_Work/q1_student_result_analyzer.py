# Question 1: Smart Student Result Analyzer

try:
    with open("students.csv", "r") as file:
        for line in file:
            try:
                student_id, name, m1, m2, m3 = line.strip().split(",")
                total = int(m1) + int(m2) + int(m3)
                percentage = total / 3

                if percentage >= 90:
                    grade = "A"
                elif percentage >= 75:
                    grade = "B"
                elif percentage >= 50:
                    grade = "C"
                else:
                    grade = "Fail"

                print(name, total, percentage, grade)
            except ValueError:
                print("Invalid data:", line.strip())
except FileNotFoundError:
    print("students.csv not found")
