
#types of data collection 
#list tuple set dictionary 

#list is ordered 
#list is changable 
#list allow duplicate
#it can be number or strings or combination of both

list ="om","ram","sham"
print(list)

list2=['banana','apple','orange']
print(list2)

#access perticular element
print(list[2])

list2.append("hook")
print(list2)

list2.remove("banana")
print(list2)

list2.insert(1,"kiwi")
print(list2)

list3=[True,False,False,False,False]
print(list3)

print(type(list3))

#use constructor for list
# thislist = list(("apple", "banana", "cherry"))
# print(thislist)


#tuples
#tuples are ordered 
#tuples are unchangable
#allows duplicate

tuple1=("omi","homi","brocode")
print(tuple1)
print(type(tuple1))

tuple2=tuple(("apple", "banana", "cherry"))
print(tuple2)


#sets 
#would't allow duplicates
#not ordered 
#not changable

set1={"apple","banana","cherry","rookie"}

print(set1)

set2=set(("apple", "banana", "cherry","rookie"))
print(set2)

set3=set(("apple", "banana", "cherry",True,1))
#values 1 and True considered as same value in sets keeps one value which arrived 1st 
print(set3)
print(type(set3))

#iterate over set
for i in set3:
    print(i)

#checks element is there inside array or not
print("apple" in set3)    

#add method helps to add element to existing set3
set3.add("HELLO WORLD")
print(set3)


#to update it can be any iterable object
set3.update({"rama","shama","looma"})
print(set3)

print(set3.remove("looma"))
#remove raises error and discard not

#clear empties set
print(set3.clear())

del set3
# print(set3) 
# error because set3 is deleted

#PYTHON DICTIONARY
#data in key=value pain
# syntax dict1={name:"omprasad"}
dict1={"name":"omprasad","age":24}

print(dict1)

#create dictionary with dict constuctor
dict2=dict(name="omprasad", age=24,gen='men')
print(dict2)

family={
    "parents":{
        "father":"Loki",
        "mother":"Mom"
    },
    "children":{
        "child1":"Raam",
        "child2":"Lakshman"
    }
}

print(family.get("children").get("child1"))

print(family["children"]["child1"])

