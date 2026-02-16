class Employee:
    # Class Attribute
    raise_amount = 1.05  # 5% raise

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        # Regular method using 'self' and the class attribute
        self.salary = int(self.salary * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        # Class method using 'cls' to change the shared attribute
        cls.raise_amount = amount

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

# Change the raise amount for the whole company using the class method
Employee.set_raise_amount(1.10)  # Now it's a 10% raise

emp1.apply_raise()
print(emp1.salary)  # Output: 55000 (Applied the 10% raise)