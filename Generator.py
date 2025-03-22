# generator to create generator object and store yeild values 
def squares(length):
    for n in range(length):
        yield n**2

for square in squares(11):
    print(square)