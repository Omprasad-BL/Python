# set in python used for storing data in uniue manner
#  set would't allow duplicate
#  set values can be modified
#  set is heterogeneous
#  set elements can be removed

set1 = {"apple", "banana", "cherry"}
print(set1.pop())

print(set1)

# you can add elements to it
set1.add("orange")

# you cannot modify using index based idea
# set1[2]="new "
# print(set1)

set1.update({"apple":"carrot"})
print(set1)

# different type of elements 
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# you can list items to set
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) #values added to ild set

# discard to remove perticular element
thisset.discard("banana")
print(thisset)

# to remove all elements use clear
thisset.clear()
print(thisset)

# or you can use del keyword

del thisset
# print(thisset)  # this will give error because set is deleted

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.

# The remove() method removes the specified element from the set.

# This method is different from the discard() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.

