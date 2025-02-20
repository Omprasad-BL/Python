num=13
sum=num
x=num
while sum>9:
    sum=0
    while x!=0:
        d=x%10
        sum+=d**2
        x//=10
    x=sum
if(sum==1 or sum==7):
    print(num, "is a happy number")
else:
    print(num, "is not a happy number")
