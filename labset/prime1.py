num=17
flag=False
for i in range(2,num+1):
    if num%i==0:
        flag=True
        break

if flag:
    print(num, "is  a prime number")
else:
    print(num, "is not a prime number")