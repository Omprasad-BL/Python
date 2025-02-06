# Function is set of statements within a block to achieve the common goal
# as term itself says Function it do some perticular functionality/work

def func():
    print("I am a function")
func()

# functions with arguments
def funcArg(name):
    print("I am a function with argument  ",name)
funcArg("Nivk")    

# function with default parameters
def funcArg1(name,age=20):
    print("I am a function with argument  ",name)
    print("My age is ",age)

# now age overrides default age
funcArg1("Nivk",30)

