class Add:
    def __init__(self):
        self.num1 = num1
        self.num2 = num2

    def add(self, a,b):
        return a + b

if __name__ == "__main__":
    print("Addition")
    num1= int(input("enter num1 \n"))
    num2= int(input("enter num2 \n"))
    add = Add()
    print("Sum of two numbers ")
    print(add.add(add.num1, add.num2))  # Output: 15        