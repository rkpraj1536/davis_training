# Question 8: Employee Attendance Tracker

attendance = {}

with open("attendance.csv", "r") as file:
    for line in file:
        emp_id, date, status = line.strip().split(",")

        if emp_id not in attendance:
            attendance[emp_id] = {"Present": 0, "Absent": 0}

        attendance[emp_id][status] += 1

for emp_id, data in attendance.items():
    total = data["Present"] + data["Absent"]
    percentage = (data["Present"] / total) * 100

    print(emp_id, data, percentage)

    if percentage < 75:
        print("Low Attendance:", emp_id)
