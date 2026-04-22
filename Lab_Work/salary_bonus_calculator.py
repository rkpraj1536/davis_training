# 6. Salary Bonus Calculator

def calculate_bonus(salary, experience_years):
    if experience_years > 10:
        bonus = salary * 0.20
    elif experience_years >= 5:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05

    return bonus

employee_count = int(input("Enter number of employees: "))

for employee_number in range(1, employee_count + 1):
    salary = float(input(f"Enter salary of Employee {employee_number}: "))
    experience_years = float(input("Enter years of experience: "))

    if salary < 0 or experience_years < 0:
        print("Invalid Input")
    else:
        bonus = calculate_bonus(salary, experience_years)
        total_salary = salary + bonus

        print(f"Bonus = {bonus}")
        print(f"Total Salary = {total_salary}")
        print()
