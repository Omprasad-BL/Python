# A simple decorator function used to add additional features to funciton
# its just like function need to wrapped with wrapper funciton
def decorator(func):
  
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function
@decorator
def greet():
    print("Hello, World!")

greet()



# Using *args and **kwargs Together
# You can use both *args and **kwargs in the same function.
#  *args for literal / positional arguments and **kwargs for keyword arguments which have key value pair
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

display_info(1, 2, 3, name="Alice", age=25)