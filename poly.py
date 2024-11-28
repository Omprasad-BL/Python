class Car:
    def __init__(self,brand,model):
        self.model = model
        self.brand = brand
    def move(cls):
        print("Car Moving") 
class Bike:
    def __init__(self,brand,model):
        self.brand = brand
        self.model=model
    def move(cls):
        print("Bike MOving") 

class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model=model
        
    def move(cls):
            print("Plane  MOving")     



obj1=Car("Tata","nano")
obj2=Bike("Hero","i20")
obj3=Plane("Boeng","C294")

for x in (obj1,obj2,obj3):
    x.move()