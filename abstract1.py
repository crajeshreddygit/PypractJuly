from abc import abstractmethod, ABC

class Vehicle(ABC):

    @abstractmethod
    def NoofWheels(self):
        pass

class Bus(Vehicle):
    def NoofWheels(self):
        return 6

b = Bus()

print(b.NoofWheels())

