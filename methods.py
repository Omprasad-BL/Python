#classes 
class Parents:
             @classmethod
             def about(cls):
                     print("Its parents method")

             @classmethod
             def message(cls):
                 print("Hello we are alive")
class Childs(Parents):
             @classmethod 
             def  about(cls):
                print("Its child method")

if __name__ == "__main__":
        obj= Childs() 

        obj.about()
        obj1=Parents()  
        obj1.message()
        obj1.about()