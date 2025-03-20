
# gcd using recusrion
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

# gcd using while loop
def gcd2(a,b):
    while(b):
        # a,b=b,a%b #this trick use simaltaneous assignment trick 
        # below is indeed to make sure value used properly
        temp=b
        b=a%b
        a=temp
    return a


print(gcd(10,30))
print(gcd2(48,18))
