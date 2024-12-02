name="NivkBoy"
age=25
address="hello world"

print( f" \n name: {name} \n age: {age} \n address:{address}")


#changing int to decimal with conversion
print( f" \n name: {name} \n age: {age:.2f} \n address:{address}")

print(f"Hey {name.upper()} you are Hero never give up")

#using formatter
#uses placeholder to add  values in between print lines
string= "hello iam {} my age is {} and my address is {}"

print(string.format(name,age,address))




