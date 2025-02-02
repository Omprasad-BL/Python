import random
import calendar
print(random.random())
print(random.randint(1,10))

print("5 km in miles is {0}".format(5*0.62137119))
print("5 mile in km is {0}".format(3.10*1.609))

print("celcius to faranhiet of 5 is {0}".format(5*(9/5)+32))
print(calendar.month(2024,2))
#print(calendar.calendar(2024))


year=2024
if((year%4==0 and year%100!=0) or (year%400==0 and year%100==0) ):
    print("leap year ")
else:
	print("not leap year")
    
prime=13
flag=True
for i in range(2,prime+1//2):
	if(prime%i==0):
		flag=False
		break   
	
if(flag):
	print(prime, "is a prime number")
else:
	print("is not a prime number")
	
	