import datetime as dt


print(dt.datetime.now())
x=dt.datetime.now()

print(x.year)
print(x.strftime('%A'))
print(x.strftime('%a'))

#constructor
print(dt.datetime(2024,4,3))

#identifying morning or evening
print(x.strftime("%p"))

#local date
print(x.strftime("%x"))

#local time
print(x.strftime("%X"))

# centuries
print(x.strftime("%C"))

# month
print(x.strftime("%b"))
print(x.strftime("%B"))

#week number
print(x.strftime("%V"))

#weekday
print(x.strftime("%u"))


#seconds
print(x.strftime("%S"))

#Minutes
print(x.strftime("%M"))

#ISO 12 hour based time
print(x.strftime("%I"))

#hours
print(x.strftime("%H"))


print(x.strftime("%G"))





