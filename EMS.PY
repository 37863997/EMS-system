#  The class Employee is the base class
class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Base Salary: {self.base_salary}"

    def calculate_salary(self):
        return self.base_salary

#  Class FullTimeEmployee is a derieved class of the class employee
class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, benefits):
        super().__init__(name, employee_id, base_salary)
        self.benefits = benefits

    def __str__(self):
        return (f"Full-Time Employee ID: {self.employee_id}, Name: {self.name}, "
                f"Base Salary: {self.base_salary}, Benefits: {self.benefits}")

    def calculate_salary(self):
        return self.base_salary + self.benefits

# The class PartTimeEmployee is A Derievd class of the Employee Class
class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id, hourly_rate * hours_worked)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def __str__(self):
        return (f"Part-Time Employee ID: {self.employee_id}, Name: {self.name}, "
                f"Hourly Rate: {self.hourly_rate}, Hours Worked: {self.hours_worked}")

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for employee in self.employees:
            print(employee)

    def calculate_total_salary(self):
        total_salary = sum(employee.calculate_salary() for employee in self.employees)
        return total_salary


# implementation of the ems
if __name__ == "__main__":
    company = Company()

    emp1 = FullTimeEmployee("Jesse mugo", 1, 20000, 40000)
    emp3=FullTimeEmployee("Mary Njeri",3,15000,23000)
    emp2 = PartTimeEmployee("Janet Njane", 2, 60, 80)
    emp4=PartTimeEmployee("Mbithi Duncan",4, 40,120)

    company.add_employee(emp1)
    company.add_employee(emp3)
    company.add_employee(emp2)
    company.add_employee(emp4)

    company.display_employees()
    print(f"Total Salary Expense: {company.calculate_total_salary()}")
