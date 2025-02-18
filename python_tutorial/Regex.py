import re
# regex is sequence of characters that forms search pattern for text
text= "its a silicon city viltrus"
x=re.search("a.*us$",text)
print(x)

print(x.start())

txt = "The rain in Vallay"
x = re.findall("ai", txt)
print(x)
#  if no match found then return empty list

# if you want to split a string where white space is there
x="Hello coding buddies how are you"
y=re.split("\s",x)
print(y)

# if you want to split a string only at 1st occurence
y=re.split("\s",x,1)
print(y)


# replace which word you want to replace
y=re.sub("\s+"," Good ",x)
# return a string with modifications
print(y)

#  you can specify how many time it should replace
# here only two times replacing
y=re.sub("\s+"," New ", x, 2)
print(y)

# if match found you will get match object else None

# getting span index of word start from which index and ends in which index
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

