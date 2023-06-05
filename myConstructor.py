
class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def info(self):
        print(f"Hii my name is {self.name} and my roll no. is {self.roll}.")

a = Student("Akash",2)
b = Student("Arvind",5)

a.info()
b.info()