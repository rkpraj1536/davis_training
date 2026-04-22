# Question 19: Error Log Reporter

errors = {}

with open("error_log.txt", "r") as file:
    for line in file:
        error_type = line.strip().split(":")[0]
        errors[error_type] = errors.get(error_type, 0) + 1

with open("summary.txt", "w") as file:
    for error, count in errors.items():
        file.write(f"{error}: {count}\n")
