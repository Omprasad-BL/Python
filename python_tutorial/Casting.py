# casting  is changing data from one type to another
# we have two types of casting 
# IMPLICIT TYPE CASTING AND EXPLICIT TYPE CASTING 
# implicit happens automatically because widened conversions have no loss of data
# explicit should done forcefully because it is narrow conversion HERE WE MAY LOSS DATA

# implicit type conversions
x=10
y=20.4
z=30j
print(x+y+z)

#explicit type casting
one=10
two='10'
print(one+int(two))

