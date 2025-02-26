# overriding in python
# unlike other languages python perform overload differently
from multipledispatch import dispatch
class Overload:

    @dispatch(int,str)
    def myfunc(i,s):
        print("method working for int and str ")
    
    @dispatch(int,int)
    def myfunc(i1,i2):
        print("method working for int and int ")
    
    @dispatch(str,bool)
    def myfunc(s,b):
        print("method working for str and bool ")

if(__name__=="__main__"):
    obj=Overload()
    obj.myfunc(10,"hello")
    obj.myfunc(10,10)
    obj.myfunc("hello",True)