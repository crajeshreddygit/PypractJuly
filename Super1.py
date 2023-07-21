class P:
    def m1(self):
        print("Parent m1 method")

class C(P):
    def m1(self):
        super().m1()
        print("Child m1 method")

c = C()
c.m1()
