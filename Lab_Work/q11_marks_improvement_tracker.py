# Question 11: Marks Improvement Tracker

exam1 = {"A": 50, "B": 60, "C": 70}
exam2 = {"A": 70, "B": 65, "C": 75}

for student in exam1:
    if exam2[student] > exam1[student]:
        improvement = ((exam2[student] - exam1[student]) / exam1[student]) * 100
        print(student, "Improved by", improvement, "%")
