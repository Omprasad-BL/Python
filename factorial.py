def factorial():
    num = int(input("Enter a number: "))
    result = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers.")
    elif num == 0:
        print("The factorial of 0 is 1.")
    else:
        for i in range(1, num + 1):
            result *= i
        print("The factorial of", num, "is", result)
factorial()        


def fact_rec(num):
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers.")
    elif num == 0:
        return 1
    else:
        return num * fact_rec(num - 1)
num = int(input("Enter a number: "))
val=fact_rec(num)
print(val)