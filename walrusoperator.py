
# The walrus operator (:=) lets you assign a value while using it in 
# an expression—making code shorter and more efficient. Here are some simple examples:
while (value := input("Enter something: ")) != "quit":
    print(f"You entered: {value}")


# Find all numbers whose squares are greater than 10:
numbers = [1, 2, 3, 4, 5]
squared = [square for n in numbers if (square := n**2) > 10]
print(squared)  # Output: [16, 25]
