
for i in range(10,20):
    flag=True
    for j in range(2,i):
        if(i%j==0):
            flag = False  
            break
    if flag:    
         print("it is palindrome ",i)
    # else:
    #     print("it is not palindrome ",i)        
      