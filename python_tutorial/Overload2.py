class Overload:
    def myfunc(self,a=None,b=None,c=None):
        # if parameters are integers
        if(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
            print(f"{a} and {b} and {c} are integer types ")
            
        elif(isinstance(a,int) and isinstance(b,int)):
            print(f"{a} and {b} are integer types ")

        elif(b==None and a==None and c==None):
            raise ValueError("Please enter values ")
        # if paramters are strings
        elif(isinstance(a,str) and isinstance(b,str) and isinstance(c,str)):
            print(f"{a} and {b}  and {c} is string type ")

        elif(isinstance(a,int) and isinstance(b,str) and isinstance(c,str)):
            print(f"{a}  is integer type {b}  and  {c} is string type ")

        elif(isinstance(a,str) and isinstance(b,int),isinstance(c,int)):
            print(f"{a} is string  {b}  and {c} is integer type ")

        else:
            print("some errors try again ")
            
        
obj=Overload()
# obj.myfunc("Nivk",24)
# obj.myfunc() #raises RuntimeError
obj.myfunc(23,300)
obj.myfunc("Nivk",23,45)
num=4000
obj.myfunc(num,"Kowoo","Raja")