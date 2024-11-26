#ITERATOR IS AN OBJECT WHICH CONTAINS COUNTABLE NO OF VALUES
# iterator object implements interator object 
#having two methods __iter__ and __next__

#string is also iterable object
name="Nivk"

names=["Nick","Johny","Subel","John"]
#iter and next method helps to access elements within iterable object
myiter=iter(names)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


for x in name:
    print(x)

for x in names:
    print(x)    



class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)    



