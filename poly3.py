# setback with this method is 
# pyhton uses dictionary for storing methods
# python so every method name stored only once
# and latest method defined will be replaced 
# SO THIS METHOD IS NOT CONVINIENT WAY FOR OVERLAODING

class Po:
    def product(self,a, b):
       p = a * b
       print(p)

# Second product method
# Takes three argument and print their
# product


    def product(self,a, b, c):
      p = a * b*c
      print(p)

# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method

if __name__ == '__main__':
    obj=Po()
    obj.product(4, 5, 5)