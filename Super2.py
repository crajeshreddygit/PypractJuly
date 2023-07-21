class A:
    def m1(self):
        print("A Class")
class B(A):
    def m1(self):
        print("B class")
class C(B):
    def m1(self):
        print("C class")
class D(C):
    def m1(self):
        print("D class")
class E(D):
    def m1(self):
        #C.m1(self)
        super(C,self).m1()

o = E()
o.m1()

