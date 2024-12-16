year=2023

if year%4==0:
    if year%100==0:
        leap=False
    elif year%400 :
        leap=True
    else  :
        leap=False
else:
    leap=False

if leap:
  print(year, "is a leap year")
else:
    print(year, "is not a leap year")