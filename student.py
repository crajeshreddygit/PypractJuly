
# commit to release_07.2023
class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def talk(self):
        print("My name is :", self.name)
        print("My roll number is : ", self.rollno)
        print("My Marks are : ", self.marks)


so = Student("sunny", 101, 90)
so.talk()
