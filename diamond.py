# problem diamond problem
# solution 
# python uses CE LINEARIZATION algorithm to avaid these kind of problems
# python use METHOD ORDER EXECUTION  strategy to resolve conflit when same methods inherited from multiple classes

#   A
# B   C
#   D


class A:
    def methodX(self):
        print("A's methodX")

class B(A):
        def methodX(self):
            print("B's methodX")

class C(A):
        def methodX(self):
            print("C's methodX")

class D(B, C):
        pass

d = D()
d.methodX() # Output: B's methodX (because B is listed first in D's inheritance)