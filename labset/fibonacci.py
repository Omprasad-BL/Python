def fib(num):
    a=0
    b=1
    if num<0:
        print("incorrect number")
    elif num==0:
        return 0
    elif num==1:
        return b
    else:
        for i in range(2,num+1):
            c=a+b
            a=b
            b=c
        return b
print(fib(9))