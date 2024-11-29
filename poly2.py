class Super:
    num = 100
    def message(self):
        print("Hello from Super class")

class Sub(Super):
    def message(self, msg=None):  # Overridden instance method
        if msg is None:
            print("hello iam overloading method {}".format(msg))
        else:
            print("simple message block")


if __name__ == "__main__":
    a = Sub()
    a.message()  # Calls the first instance method
    a.message("I am overloaded method")  # Calls the overridden instance method
    print(a.num)