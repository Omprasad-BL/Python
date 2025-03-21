from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def swim(self):
        pass


class Turtle(Animal):
    def walk(self):
        print("walking")

    def swim(self):
        print("Swimming")


class Fish(Animal):
    def walk(self):
        try:
            raise Exception('The Fish cannot walk')
        except Exception:
            print("it can only swim in water ")
    def swim(self):
        print("Swimming")


Fish().walk()
Turtle().walk()