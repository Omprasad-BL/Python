import builtins

name="omprasad"
name1="omprasad"


print(id(name), "   ", id(name1))

list=[1,2,3]
list1=list
list1.reverse()

print(list, "   ", list1)
print(id(list), "   ", id(list1))

val=[]
print(val)
val=" "
print(val)

# print(dir(builtins))

builtin = [name for name in dir(builtins) if callable(getattr(builtins, name))]
print(builtin)
