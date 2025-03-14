arr=[1,2,4,56,67,7,6]
b,c,*d=arr
print(b,c,d)

# one liner
arr=[x for x in arr if x%2==0 ]
print(arr)

#fact
fact=lambda x:x and  x*fact(x-1) or 1
print(fact(5)) 

