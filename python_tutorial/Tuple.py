# tuples are list of items similar to to list
# in tuples items are immutable
# in tuples items can be same
#  tuple can be any kind
# follows inserted order
#  tuple are represented withing rounded brackets 
tuple1 = (1, 2,2, 3, 4, 5)
print(tuple1)
# tuple1[1]=243 error

print(tuple1[2])
# accessing

# creating with tuple constructor
tuple2 = tuple((1, True, "Hellow ", 4.00, 5j))
print(tuple2)

# finding tuple class 
print(type(tuple2))

print(tuple2.count("Hellow "))

# NOTE even 1 also considerd as True