#class is a blue print of realtime  object like bus person tree so on
#class methods need object for accessibality.
#class have constructor (default,parameter)
#constructor invokes only when objects are created
# @ staticmethods belong to class but not to it's instances so access using class names
# @staticmethods called before constructor because they are in static pool
class One:
    def __init__(self):
        print("constructor invoked")
    @classmethod
    def profile(cls):
        print("Hwe are coders from small town")
    @staticmethod
    def message():
        print("nothing is for free!")

if __name__=='__main__':
    obj= One()
    obj.message()
    One.profile()

#INHERITENCE
#you can inherit super class methods and variables to child class with this
#you can override parent class methods if you don't want that


#extends
class Two(One):
    def __init__(self):
        print("Two's constructor intitialized")


class Three(One):
    def chat(cls):
        print("hello iam chat bot")

#python solves diamond problem by allowing access to 1st parent object
if __name__=='__main__':
    obj2=Two()
    obj2.message()
    obj2.profile()
    obj3=Three()
    obj3.profile() 
    obj3.chat()



