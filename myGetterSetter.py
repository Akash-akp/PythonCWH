
class MyClass:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    @property
    def getName(self):
        return self.name

    @getName.setter
    def setName(self,newName):
        self.name = newName


a = MyClass('Akash',45)
print(a.getName)
a.setName = 'Arvind'
print(a.getName)

