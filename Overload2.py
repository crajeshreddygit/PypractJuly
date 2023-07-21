class Emp:
    def __init__(self,name,wage):
        self.name = name
        self.wage = wage

    def __mul__(self, other):
        return self.wage * other.daysworked

class TS:
    def __init__(self,name,daysworked):
        self.name = name
        self.daysworked = daysworked

E = Emp("Reddy",1000)
T = TS("Reddy",50)

print(" Total wage  for {} is :  {}".format(E.name ,E*T))
