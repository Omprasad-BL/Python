# variable is a container to store values in memory location
# python variables are dynamic 
# python is speed interpred and dynamic scripting language

# normal variable
x="Nivk"
print(x)
# you can change variable at any time

# assign multiple values to multiple variables
a,b,c=10,20,30
print(a,b,c)

# assign same value to multiple variable
a=b=100
print(a,b)


# TYPE CONVERSION
# converting from one data type to another is called type conversion
# TWO TYPES OF CONVERSIONS
# implicit type conversion automatic type conversion here no loss of data
# explicit type conversion manual type conversion here loss of data
# explicit
one=10
two='20'

# print(one+two)
print(one+int(two),'manually converted from string 20 to int 20 ')
print("here loss of data happens")

# implicit

one=10
two=20.5
print(one+two,"autmatically converted to float from int ")

nums=(10,30)
s,a=nums
print(s,a)

arr=[1,2,3,4,5,6,7]
val1,val2,*val3=arr

print(val1,val2,val3)

people = [
	("Bob", 42, "Mechanic"),
	("James", 24, "Artist"),
	("Harry", 32, "Lecturer")
]

for name, age, profession in people:
	print(f"Name: {name}, Age: {age}, Profession: {profession}")
	

example_list = ["A", "B", "C"]

for counter, letter in enumerate(example_list):
	print(counter, letter)

# print( chr('64'), ord('A') )

# print("Nivk ", end=' ', flush='False',file='sys.stdout',sep='\n')

aa="omprasad b l"

print(tuple(aa))

print(list(aa))

print(set(aa))

# Operators
# relational operators
# arithmetic operators
# logical operators
# comparison operators
# identity operators
# membership operators
# arithmetic operators
# assignment operators


# member and identity operators
a,b=10,10
print(a is b)
