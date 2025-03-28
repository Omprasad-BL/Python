
# python hidden tricks

# Python follows the LEGB (Local → Enclosing → Global → Built-in) rule to look up variables.
# global and nonlocal used manage scope of variable 
# global used to assign value to a variable from anywhere when same variables are are there

# nonlocal is made for assign value to parent scope if not throws exception
# if variable same declare nonlocal to mention changes made for parent scope variable

x = 10  # Global

def outer():
    x = 20  # Enclosing
    def inner():
        x = 30  # Local
        print(x)  # 30
    inner()
outer()
print(x)  # 10 (Global)


# mutable default argument in python
# here items in immutable keeps changes as python reads paramters only once
# item is immutable

def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]  (Unexpected!)


# new method have 1st preference because it creates object the __init__ method intialize variables to it
class Example:
    def __new__(cls):
        print("Creating instance")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing instance")

obj = Example()

# PY "is" and "=="
#  is used to compare references
x=[1,2,3]
y=[1,2,3]
print(x is y)
print(x==y)

# slot mechanism
# Prevents creating dynamic attributes, saving memory.
class Person:
    # remove 'address to see attribute error'
    __slots__ = ['name', 'age','address']

p = Person()
p.name = "Alice"
p.age = 25
p.address = "NYC"  # AttributeError



# ASYNCH FUNCTIONS MUST BE AWAITED IN PYTHON
import asyncio

async def main():
    print("Start")
    await asyncio.sleep(2)
    print("End")

asyncio.run(main())
