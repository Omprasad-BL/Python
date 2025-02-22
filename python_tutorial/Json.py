# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# we need to import json module

import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
# to print data
print(json.loads(x))

# if you want perticular peice then mention that
print(json.loads(x)['age'])

x={
    "name":"Nivk",
    "age":30,
    "city":"New York",
    "hobbies":["Reading","Cooking","Coding"]
}

# to convert python dictionary to json string
y=json.dumps(x)
print(y)


# You can convert Python objects of the following types, into JSON strings:
# dict,list,tuple,string,int,float,True,False,None

# Convert a Python object containing all the legal data types:
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

print(json.dumps(x))

# adding your own key value seperator
print(json.dumps(x,indent=4,separators=(". "," : ")))

# use sort_keys to sort all elements in object
print(json.dumps(x,sort_keys=True,indent=2))

from types import SimpleNamespace

data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
print(x)
