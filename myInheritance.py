
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetail(self):
        print(f"The name of Employee id: {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print("My favorite language is Python")


a = Employee("Akash",334)
b = Programmer("Jyoti",445)

# a.showLanguage(); # will show error as function is not available in employee class
b.showLanguage();
