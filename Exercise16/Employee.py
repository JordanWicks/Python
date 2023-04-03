from Person import Person
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")


# Creating an instance of Employee and calling it
employee = Employee("John", 35, "E1234", 50000)
employee.print_info()


