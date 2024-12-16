num=3
sum=0   
for i in range(1,num+1):
     sum += i
    
print("sum is " , sum)    

num1=3
def sum(num1):
     if num1==1:
         return 1
     else:
         return num1+sum(num1-1)
print("sum is ", sum(num1))