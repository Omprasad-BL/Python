import os
def addition(a,b):
        return a + b
    
def subtraction(a,b):
        return a - b
def division(a,b):
        if b > 0:
            return a // b
        else:
            return "Error: Division by zero"
def multiplication(a,b):
            return a * b
def mod(a,b):
         return a % b




     
while True:
    #  os.system("cls")
     print("press 1.Addition")
     print("press 2.Subtraction")
     print("press 3.Multiplication")
     print("press 4.Division")
     print("press 5.Modulus")
     print("press 6.Exit")
     opt=int(input("enter option"))
     num1=int(input("enter num1"))
     num2=int(input("enter num2"))
    #  try:
    #       if num2<0:
    #            raise Exception
    #  except Exception as e:
    #       print("Error: Negative number not allowed in this operation")
          
          
    
     if opt==1:
        print(addition(num1, num2))
     elif opt==2:
        print(division(num1,num2))
     elif opt==3:
        print(multiplication(num1, num2))
     elif opt==4:
        print(division(num1, num2))
     elif opt==5:
        print(mod(num1, num2))
     elif opt==6:
        exit(0)
     else:
        print("invalid option try another")      
               



#os.system('cls')    