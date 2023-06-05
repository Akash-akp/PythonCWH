class Employee:
    company = "Apple"
    number = 0

    def __init__(self, name, raise_amount):
        self.name = name
        self.raise_amount = raise_amount

    def info(self):
        print(
            f"The employee name is {self.name} and raise amount of this employee is {self.raise_amount}. He/She is working in {self.company}")


Employee.company = 'Microsoft'
a = Employee("Akash", 0.2)
a.company = 'Google'
a.info()
b = Employee("Jyoti", 0.8)
b.info()

