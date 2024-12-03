#file handling in pyhton
#open() used to read and open file
# constains 2 parameters 1st for file name and 2nd for file operations
# ex open(hello.txt, "rt") here in 2nd parameter r means "read" t means "text" text is assigned by default

f=open("iter.py","rt")
#read is used to read  file 
# print(f.read())

#prints only first 5 characters 
# print(f.read(5))

#you can read line by line
print(f.readline())
print(f.readline())


#iterating each line using for loop
f1=open("iter.py","rt")
for x in f1:
    print(x)

#to close the file
f.close()    