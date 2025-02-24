
# python file handling
x=open("details.txt",'r')
# read allows to read all content in file
print (x.read())
# you can also mention what kind data b or t means binary or text

# you can print exact characters how much you want
x.close()
# to reopen you have to close it
x=open("details.txt",'r')
# print(x.read(5))
print(x.readline())
# to read only one line use readline() 

x.close()
# to append data to existing file use a tag in open()
x=open("details.txt",'a')

x.write("\nNew Data")
x.close()

# after modification openning and adding details
x=open("details.txt",'r')
print(x.read())
x.close()

# to create new file use a tag in open() with x as second argument

x=open("newfile.txt",'x')
x.close()


# to delete file use os module
import os
# x=os.remove("newfile.txt")
# to remove folder use rmdir("filename")
if os.path.exists('newfile.txt'):
    print("File deleted successfully")
    os.remove("newfile.txt")
else:
    print("The file does not exist")