from abc import ABC,abstractmethod

class Car(ABC):
    def __init__(self,brand, model,year):
        self.brand=brand
        self.model=model
        self.year=year


    @abstractmethod
    def printDetails():
        pass
    def accelerate(self):
        print("speed speed ")

    def breakApplied(self):
        print("Car stopped ")
    
class Suv(Car):
    def printDetails(self):
        print(self.brand)
        print(self.model)
        print(self.year)

    def sunRoof(self):
        print("Available   ")

# these below things generate error because all classes not given defination
# obj=Car()
# obj.accelerate()

# this part works
obj1= Suv('Tayota','fortunar',2022)
obj1.printDetails()
obj1.accelerate()
obj1.breakApplied()