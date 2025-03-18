arr=[1,2,4,56,67,7,6]
b,c,*d=arr
print(b,c,d)

# one liner
arr=[x for x in arr if x%2==0 ]
print(arr)

#fact
fact=lambda x:x and  x*fact(x-1) or 1
print(fact(5)) 

# enumarations over element with proper indexing
names = ['Alice', 'Bob', 'Cathy']

for index, name in enumerate(names):
    print(index, name)



# zip method to zip 3 lists
names = ['Alice', 'Bob', 'Cathy']
ages = [25, 30, 35]

paired = list(zip(names, ages))
print(paired)  # Output: [('Alice', 25), ('Bob', 30), ('Cathy', 35)]

# unzip zipped things
ids=[1,2,3]
grades=['A','B','C']
zipped = zip(ids, names, grades)
unzipped = list(zip(*zipped))
print(unzipped)  # Output: [(1, 2, 3), ('Alice', 'Bob', 'Cathy'), ('A', 'B', 'A+')]

numbers=ages
# reverse a list
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # Output: [9, 5, 4, 3, 2, 1, 1]

#  use of f-strings is to print an identifier name along with the value. This was introduced in Python 3.8.


x = 10
y = 20
print(f"{x = }, {y = }")

"""
x = 10, y = 20
"""

password = "ABCabc123"
print(password.isalnum())

"""
True
"""


# this dictionary also do same thing as passing arguments whe you pass it as **kwargs
# means keyword arguments
dictionary = {"a": 1, "b": 2}

def someFunction(a, b):
    print(a + b)
    return

# these do the same thing:
someFunction(**dictionary)
someFunction(a=1, b=2)


x = [1, 2, 3]
y = map(lambda x : x + 1 , x)
print(list(y))


# python class
class someClass:
    def __repr__(self):
        return "<some description here>"

someInstance = someClass()

# prints <some description here>
print(someInstance)



# python now let's you have standalone virtual environment for each project
# SO YOU DON'T GET ANY VERSION CONFLICT FOR EACH PROJECT 


# python -m venv my-project
# source my-project/bin/activate
# pip install all-the-modules
# Now you can have standalone versions and installations of Python running on the same machine. Sorted!