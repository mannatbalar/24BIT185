# Sample employee data as a list of dictionaries
employees = [
    {'dept_no': 101, 'emp_roll': 'E001', 'salary': 50000},
    {'dept_no': 101, 'emp_roll': 'E002', 'salary': 60000},
    {'dept_no': 102, 'emp_roll': 'E003', 'salary': 45000},
    {'dept_no': 102, 'emp_roll': 'E004', 'salary': 70000},
    {'dept_no': 103, 'emp_roll': 'E005', 'salary': 52000},
    {'dept_no': 103, 'emp_roll': 'E006', 'salary': 49000},
]


dept_salaries = {}

for emp in employees:
    dept = emp['dept_no']
    salary = emp['salary']
    
    if dept not in dept_salaries:
        dept_salaries[dept] = []
    dept_salaries[dept].append(salary)


for dept, salaries in dept_salaries.items():
    print(f"Department {dept} -> Min Salary: {min(salaries)}, Max Salary: {max(salaries)}")
