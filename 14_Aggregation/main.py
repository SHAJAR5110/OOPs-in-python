
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")


class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: reference to an existing Employee object

    def display_department_info(self):
        print(f"Department: {self.dept_name}")
        print("Employee Info:")
        self.employee.display_info()


emp1 = Employee("Shajar", 101)

dept1 = Department("Software Engineering", emp1)

dept1.display_department_info()
