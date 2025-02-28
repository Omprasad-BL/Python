# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
import datetime

x = datetime.datetime.now()
print(x)

# to create date in python
import datetime

x = datetime.datetime.now()

print(x)

# for full week day name
print(x.strftime("%A"))

# for week day in number 
print(x.strftime("%w"))

# month name full version
print(x.strftime("%B"))

# year name full version and short version
print(x.strftime("%Y"))

print(x.strftime("%y"))


# hour minute seconds
print(x.strftime("%H"),"  ", x.strftime("%M")," ", x.strftime("%S"), x.strftime("%p"))

# week number of year
print(x.strftime("%W"))

# local version of date

print(x.strftime("%x"))

# local version of time

print(x.strftime("%X"))


