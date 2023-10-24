class Student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def __str__(self):
        #return self.name
        return ' name :{}, rollno :{}, marks : {} '.format(self.name,self.rollno,self.marks)

s1= Student("Durga",101,95)
s2 = Student("Ravi",102,98)
print(s1)
print(s2)

