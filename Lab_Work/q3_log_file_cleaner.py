# Question 3: Log File Cleaner

unique_logs = set()
error_count = {}

with open("log.txt", "r") as file:
    for line in file:
        if "ERROR" in line and line not in unique_logs:
            unique_logs.add(line)
            error_count[line.strip()] = error_count.get(line.strip(), 0) + 1

for log, count in error_count.items():
    print(log, ":", count)
