class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color

    def getInfo(self):
        print("Car name :{}, model : {}, color : {}".format(self.name,self.model,self.color))

class Employee:
    def __init__(self,ename,eno,car):
        self.ename = ename
        self.eno = eno
        self.car = car

    def empInfo(self):
        print("Employee Name:",self.ename)
        print("Employee Number:",self.eno)
        print("Employee Car Info: ")
        self.car.getInfo()

c =Car("Innova","2.5V","Grey")

E = Employee("Rajesh",1234,c)
E.empInfo()
