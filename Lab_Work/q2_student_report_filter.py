# Question 2: Student Report Filter

with open("students.txt", "r") as student_file:
    student_records = student_file.readlines()

with open("top_students.txt", "w") as output_file:
    for record in student_records:
        record = record.strip()

        if record == "":
            continue

        student_data = record.split(",")

        if len(student_data) == 3:
            name = student_data[0]
            marks = int(student_data[1])
            city = student_data[2]

            if marks > 75:
                output_file.write(f"{name},{marks},{city}\n")

print("Filtered student records saved in top_students.txt")
