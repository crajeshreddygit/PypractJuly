class Parent:
    def m1(self):
        print("Parent m1 method")


class Child(Parent):
    def m2(self):
        print("Child m2 method")

class GC(Child):
    def m3(self):
        print("Grand child m3 method")


o = GC()
o.m1()
o.m2()
o.m3()
print(GC.__mro__)
