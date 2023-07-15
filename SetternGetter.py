class Student:
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self,marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

n = int(input("Enter number of Students"))

for i in range(n):
    s = Student()
    name = input("Enter name")
    marks = int(input("Enter Marks"))
    s.setName(name)
    s.setMarks(marks)

    print("Hi Studnet name is :",s.getName())
    print("Marks are :", s.getMarks())
    print()




