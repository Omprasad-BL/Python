# strings are are surrounded by single quotes or double quotes
# string is a set of characters
# types of string literals and normal strings
print("Hello it's Nivk ")

# assigned variable string
name="Nivk"
print("Hello ",name)

# multiline string 
about=""""hello we are from mars 
we will stay here for 
next two weeks """
print(about)

# strings are nothing but arrays os bytes representing unicode characters
# square brackets can be used to acces elements 
a="Nivk"

# length of string len()       
print(len(a))

# check string present in string
print("will" in about)

print("not_in" not in about)

# STRING METHODS
# slicing
data="Hello world"
print(data[0:5])
# slice from start
print(data[:5 ])
# slice to the end
print(data[5: ])
# negetive indexing
print(data[-5:0])

print("UpperCase Code".upper())
print("LowerCase Code".lower())
print(" spaced word ".strip())
print("hello world".split(" "))

# concat
x="Good "
y=" Boy "
print(x+y)

# F-STRING
print(f"Hello iam a {x} {y}")

# printing with decimals
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

print("hunter ".capitalize())
print("HUnter".casefold())
x="RoyalAirForce"
print(x.center(5,"A"))

print(x.count('o'))

x="Nivk Hero"
b=x.index('Hero')
print(b)

b=x.find('vk')
print(b)

b=x.endswith('ro')
print(b)

b=x.startswith('Niv')
print(b)

b=x.replace('Nivk','Nick')
print(b)

b=x.swapcase()
print(b)

b=x.rpartition(' ')
print(b)

b=x.__sizeof__
print(b)

b=x.isalnum()
print(b)

b=x.isalpha()
print(b)

b=x.isdigit()
print(b)

# given character count will be returned
b=x.count('i')
print(b)

# decimals in string
x='34.345'
b=x.isdecimal()
print(b)

# ONLY CAPITAL LETTER SHOULD BE THERE
b=x.istitle()
print(b)

b=x.islower()
print(b)    

b=x.isupper()
print(b)

x='Hello Nivk {0}'
b=x.format('is super hero')
print(b)

