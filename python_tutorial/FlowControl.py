# flow control is nothing but handling code blocks based on situations 
# if condition is a descision making 
# if condition meet then if block will execute otherwise else will execute

# IF CONDITION
x=10
if x>20:
    print("x is less than {0}".format(x))
else:
    print("x is greater than {0}".format(x))    

# IF-ELIF-ELSE
x=9
if x>11:
    print("x is greater than 11")
elif x>15:
    print("x is greater than 15")
else:
    print("x is less than 11 or equal to 15")

# Nested IF
if(x<15):
    if(x<10):
        print("x is less than 10")
    else:
        print("x is greater than or equal to 10")


# LOOPING Conditions
# for loop
# when you know range 
for i in range(1,5):
    print(i)

# when you don't know range
x=10
while (x!=0):
    print(x, end=" ")
    x-=1

# do while loop
# execute 1st time even condition is false
x=10
while x!=0:
    print(x, end=" ")
    x-=1


# PYTHON break and continue
# break is used to terminate LOOPS immediately
for i in range(1,5):
    if i==3:
        break
    print(i)

# continue is used to skip current iteration and move to next iteration

for i in range(1,5):
    if i==3:
        print(f"{i} skipping")
        continue
    print(i)

def fn(**a):
    for i in a.items():
        print (i)
fn(numbers=5,colors="blue",fruits="apple")

arr=[1,2,4,23,4,3]
for key,val in enumerate(arr):
    print (key,val)


my_set = {"apple", "banana", "cherry"}
for index, value in enumerate(my_set):  # Might seem to work, but index is arbitrary
    print(index, value)

my_dict = {"a": 1, "b": 2, "c": 3}


# Iterate through key-value pairs (preferred for dictionaries)
for key, value in my_dict.items():
    print(key, value)

