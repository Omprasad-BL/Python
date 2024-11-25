# import json
#JSON is used for storing and exchanging data
#JSON is text written with javascript object notation

# profile='{ "name":"Omprasad B L","age":30,"gender":"Male"}'
#print the json format
# print(json.loads(profile))

# a Python object (dict):
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x,indent=2))

#json profile
profile='{ "name":"xx ","age":25,"gender":"male","work":"it"}'
print(json.loads(profile))


y = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}


print(json.dumps(y,indent=3))