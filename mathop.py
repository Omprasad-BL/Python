#provides maths  methods to deal with basic mathematical operations


import math
#to find minimum 
x=min(10,20,30)
print(x)

y=max(10,20,30)
print(y)

#abs used to convert any negative value to positive rounded values 
print(abs(-10.00))

#to find power of number
print(pow(5,2))

print(math.sqrt(200))

# ceil rounds number in upword nearest number
print(math.ceil(10.2))

# floor rounds number in downword nearest number
print(math.floor(10.2))


# PI value
print(math.pi)

# to find factorial of number
print( math.factorial(5))


#absolute for float number converts negative to positive
print(math.fabs(-20.24))


#method return sum of values in iterable object
#any iterable object like list, tuple , set ..
nums=[1,2,3,4,5,6,7,8,9,10]
print(math.fsum(nums))


#method to check is given real number is finite number or not
print(math.isinf(float("inf")))

#check is given real number is nan (not a number type or not)
print(math.isnan(float("nan")))
print(math.isnan(float(234)))


print(math.inf)

# to cut decimal points use this method
print(math.trunc(23.43))






