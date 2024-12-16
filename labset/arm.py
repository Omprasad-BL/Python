num1=1634
# 153
copy=num1
sum=0

def power(base,exp):
    ans=0
    while exp>0:
        ans=ans*base
        exp-=1
    return ans    
    
def counter(val):
    count=0
    while val > 0:
        val//=10
        count +=1
    return count
    

while copy!=0:
    d=copy%10
    sum+= pow(d,counter(num1))
    copy//=10
if sum==num1:
    print("number is armstrong ", num1)  
else:
    print("number is not armstrong ", num1)