#  python is object-oriented programming language
#  python supports oops concept
#  python is classs based
#  python is dynamic programming language

class Person:
    def __init__(self, name, age,address="Not Given"):
        self.name = name
        self.age = age
    # instance methods
    def getName(self):  # Instance method, takes 'self'
        return self.name
    
    def details(self):
        print(f"iam {self.name} {self.age}")
        return

    def edu(self):
        print(f"{self.name} is studying")
        return 
    
    @classmethod
    def about(self):
        return "this is class method"
    
    @staticmethod
    def wish():
        print("Hell Iam a Developer")

x=Person("Omi", 25,"Coding").getName()

# print within print return None
Person("Omi", 25,"Coding ").details() 
Person.about()
Person.wish()


