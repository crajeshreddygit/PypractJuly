class engine:
    a = 10
    def __init__(self):
        self.b =2
    def m1(self):
        print('Engine Specific Functionality')


class car:
    def __init__(self):
        self.engine = engine()

    def m2(self):
        print('Car using Engine Class Functionality')
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()

c = car()
c.m2()




