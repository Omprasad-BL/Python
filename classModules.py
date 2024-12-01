class math2:
    def addition(self,a,b):
        return a + b
    
    def subtraction(self,a,b):
        return a - b
    
    def multiplication(self,a,b):
        return a * b
    
    def division(self,a,b):
        if b != 0:
            return a // b
        else:
            return "Error: Division by zero"
    def mod(self,a,b):
        if b != 0:
            return a % b
        else:
            return "Error: Division by zero"
        