import os

f=open("read.txt", "w")
#"a" means all
# print(f.read())

f.write("hello coder  nice to meet you ")
f.close()

#after appending data reading file
f2=open("read.txt", "r")
print(f2.read())

#to delete file you need os module
if os.path.exists("read.txt"):
    print("you can delete read.txt using remove method")
    # os.remove("read.txt")
else:
    print("The file does not exist")
