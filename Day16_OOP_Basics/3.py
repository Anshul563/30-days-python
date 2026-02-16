class Employee:
    def __init__(self, name, role):
        self.name = name    # Instance attribute
        self.role = role    # Instance attribute

emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Designer")

# Accessing Instance Attributes
print(emp1.name)  # Output: Alice
print(emp2.name)  # Output: Bob