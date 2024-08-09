# Define a tuple to represent an employee record
employee_1 = ("Alice Johnson", 30, "Engineer", 75000)
employee_2 = ("Bob Smith", 45, "Manager", 95000)
employee_3 = ("Carol White", 28, "Designer", 67000)

# List of employee records
employees = [employee_1, employee_2, employee_3]

# Print each employee's information
for employee in employees:
    name, age, job_title, salary = employee
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Job Title: {job_title}")
    print(f"Salary: ${salary}")
    print("-" * 20)
