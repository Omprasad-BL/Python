import math
def quad(a,b,c):
    dis_form = b*b - 4 * a*c
    sqr_val=math.sqrt(abs(dis_form))
    if dis_form>0:
        print("real and difference root ")
        print((-b-sqr_val)//(2*a))
        print((-b+sqr_val)//(2*a))

    elif dis_form==0:
        print("real and same root ")
        print(-b//(2*a))
    else:
        print("complex roots")
        print((-b/(2*a)))
        print((+b/(2*a)))

a,b,c=12,32,23
if a<0:
    print("enter correct values ")
else:
    quad(a,b,c)    