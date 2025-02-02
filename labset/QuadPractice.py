import math

def quad(a,b,c):
    desc_val= b*b - 4*a*c
    sqr=math.sqrt(abs(desc_val))
    if desc_val>0:
        print("two distinct quad")
        print(-b -sqr//2*a)
        print(-b+sqr//2*a)
    elif(desc_val==0):
        print("both are same ") 
        print(-b //2*a) 
    else:
        print("complex numbers ") 
        print(-b//2*a) 
        print(+b//2*a)
a,b,c=2,3,4
if(a<0):
    print("enter correct values and try again ")
else:
    quad(a,b,c)
