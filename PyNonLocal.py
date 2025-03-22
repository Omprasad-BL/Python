def outer():
    x = 10  # x is local to outer()

    def inner():
        y = 5  # y is local to inner()
        print(x) # x is in the enclosing scope, and is accessible.
        print(y)

    inner()
    print(x)

outer()


# non localhelps to differentiate that current scope variable is not going to modify
def outer():
    x = 10

    def inner():
        nonlocal x  # Indicate that x is from the enclosing scope
        x = 20  # Modify the x from outer()
        print("inner:", x)

    inner()
    print("outer:", x)

outer()