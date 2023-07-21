class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def __gt__(self, other):
        return self.marks > other.marks

s1 = Student("raj",199)
s2 = Student("reddy",188)
print(s1 < s2)
