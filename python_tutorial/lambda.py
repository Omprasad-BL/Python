# lambda is python functions
# lambda is used to do quick operations
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression

x = lambda a : a + 2025
print(x(23))

# passing within functions
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

