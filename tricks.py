arr=[1,2,4,56,67,7,6]
b,c,*d=arr
print(b,c,d)

# one liner
arr=[x for x in arr if x%2==0 ]
print(arr)

#fact
fact=lambda x:x and  x*fact(x-1) or 1
print(fact(5)) 

# enumarations over element with proper indexing
names = ['Alice', 'Bob', 'Cathy']

for index, name in enumerate(names):
    print(index, name)



# zip method to zip 3 lists
names = ['Alice', 'Bob', 'Cathy']
ages = [25, 30, 35]

paired = list(zip(names, ages))
print(paired)  # Output: [('Alice', 25), ('Bob', 30), ('Cathy', 35)]

# unzip zipped things
ids=[1,2,3]
grades=['A','B','C']
zipped = zip(ids, names, grades)
unzipped = list(zip(*zipped))
print(unzipped)  # Output: [(1, 2, 3), ('Alice', 'Bob', 'Cathy'), ('A', 'B', 'A+')]

numbers=ages
# reverse a list
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # Output: [9, 5, 4, 3, 2, 1, 1]

