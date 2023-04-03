from Person import Person
class Customer(Person):
    def __init__(self, name, age, customer_id):
        super().__init__(name, age)
        self.customer_id = customer_id

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Customer ID: {self.customer_id}")


# Creating an instance of Customer and calling it
customer = Customer("Mary", 28, "C5678")
customer.print_info()