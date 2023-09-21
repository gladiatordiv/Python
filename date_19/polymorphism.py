'''def add(x,y,z=0):
    return x+y+z
print(add(2,3))
print(add(2,3,4))'''
from abc import ABC,abstractmethod
class Car(ABC):
    def mileage(self):
        pass
class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")
class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph")   