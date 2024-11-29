class Args:
    def list(self,*krgs):
        for word in krgs:
            print("value is {}".format(word))
        
    def list2(self, **krgs):  # Include 'self' for instance method
        for key, val in krgs.items():
            print("key is {} and value is {}".format(key, val))        


if __name__ == "__main__":  
    x=Args()         
    x.list("apple", "banana", "orange")
    x.list2(fruit1="apple", fruit2="banana", fruit3="orange")         