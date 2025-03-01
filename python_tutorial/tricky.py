value=45
value=11
print(value)

arr=[2,4,3,6]
# indices should be integers
# arr[2.0]=20
# print(arr[2.0])

print(hash(5)==hash(5.0))
# internally hash converts float to integer

my_list = [8,4,8,2,2,5,8,0,3,5,2,5,8,9,3,8]
print("Most frequent item:", max(set(my_list), key=my_list.count))

# string format tricks
language = "Python"

# Method 1
print(language + " is my favourite programming language.")

# Method 2
print(f"I code in {language}")

# Method 3
print("%s is very easy to learn." % (language))

# Method 4
print("I like the {} programming language.".format(language))


# packing from list or tuple * should be prefix position
a, *b = (1, 2, 3)
print(a, b)


import sys
# get size of variable
a = [1, 2, 3, 4, 5]
print(f"List size: {sys.getsizeof(a)} bytes")

# generators
a = [x * 2 for x in range(10)] #returns list after calculations
b = (x * 2 for x in range(10)) # returns generator object instead of list

print(a)
print(b)

# formatting 
x = 10
y = 20
print(f"{x = }, {y = }")

"""
x = 10, y = 20
"""


# appending to sub array
a = (1, 2, [1, 2, 3])
a[2].append(4)
print(a)

"""
(1, 2, [1, 2, 3, 4])
"""