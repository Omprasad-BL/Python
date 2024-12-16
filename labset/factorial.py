
num=5
fact=1
for i in range(1, num+1):
    fact*=i
print("factorial of num is ", fact)    

num2=5
def factorial(num2):
    if num2==1 or num2==0:
        return 1
    else:
        return num2*factorial(num2-1)

print("factorial of num is ", factorial(num2))