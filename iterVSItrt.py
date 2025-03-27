
# ITERATOR
# it is an object contains property to iterate over objects
#  __iter__ , __next__

arr=[1,2,3,4]
ar=iter(arr)
print(next(ar))
print(next(ar))
print(next(ar))
print(next(ar))
# after exceeding length stop iter error will be raised



# ITERABLE
# is is an object which we can iterate over
arr=[1,2,4,2,54,23]


# a class for iter and next method implementatoin
class SimpleIterator:
    """
    A simple iterator class for iterating through a list.
    """
    def __init__(self, data):
        """
        Initializes the iterator with a list.
        """
        self._data = data
        self._index = 0

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next item in the list or raises StopIteration.
        """
        if self._index >= len(self._data):
            raise StopIteration
        current_item = self._data[self._index]
        self._index += 1
        return current_item

# Example Usage:
my_list = [10, 20, 30]
my_iterator = SimpleIterator(my_list)

print("Iterating using the iterator directly:")
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
try:
    print(next(my_iterator))  # This will raise StopIteration
except StopIteration:
    print("End of iteration")

print("\nIterating using a for loop:")
my_list_again = ['apple', 'banana', 'cherry']
another_iterator = SimpleIterator(my_list_again)
for item in another_iterator:
    print(item)