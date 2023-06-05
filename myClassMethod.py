class Student:
    School = "KV"
    def show(self):
        print(self.name,"is studying in",self.School)

    @classmethod
    def changeSchool(cls,newSchool):
        cls.School = newSchool

a = Student()
a.name = 'Akash'
a.changeSchool("DAV")
a.show()
print(a.School)
print(Student.School)

