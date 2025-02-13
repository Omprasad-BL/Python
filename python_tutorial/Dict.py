#  dictionary same as like common word dictionary
#  used to store values in key value pairs
#  dictionary would't allow duplicate keys
#  dictionary can contains nested dictionaries
#  dictionary is mutable
#  dictionary key can be any type of all should be same type
#  values are case sensitive
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    }
}
#  priting dictionary
print(my_dict)
#  accessing value by key
print(my_dict["city"])

#  updating value by key
my_dict["age"] = 31
print(my_dict["age"])

#  adding new key-value pair
my_dict["country"] = "USA"
print(my_dict)


#  deleting key-value pair

del my_dict["country"]
print(my_dict)
# deleting whole del dict name to delete whole dictionary

#  nested dictionary
nested_dict = {
    "person": {
        "name": "John",
        "age": 30
    },
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    }
}

print(nested_dict)

y=my_dict.copy()
# copied dictionary
print(y)

# updated values
y={"name":"Nivk","age":25}
y.update({"Role":"Hero"})
print(y)

# only keys
print(y.keys())

# only values
print(y.values())

# get method
print(y.get("Role"))
