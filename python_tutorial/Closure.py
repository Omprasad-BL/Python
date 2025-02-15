# closure is a mechanism which is used to hold function results even after executing
# syntax
def counter():
    count = 0  # This variable is inside counter(), but it is remembered
    def increment():
        nonlocal count  # Allows modification of `count` in the enclosing function
        count += 1
        return count
    return increment  # Return the inner function

counter1 = counter()  # Creates a new counter
print(counter1())  # Output: 1
print(counter1())  # Output: 2
print(counter1())  # Output: 3

counter2 = counter()  # Creates a new, independent counter
print(counter2())  # Output: 1



# 1️ Generating Unique IDs (Auto-Incrementing Numbers)
# Imagine you're making a ticket booking system, where each new ticket gets a unique number.

def ticket_counter():
    ticket_number = 0
    def next_ticket():
        nonlocal ticket_number
        ticket_number += 1
        return f"Ticket #{ticket_number}"
    return next_ticket

counter1 = ticket_counter()  # Create a counter
print(counter1())  # Ticket #1
print(counter1())  # Ticket #2
print(counter1())  # Ticket #3

counter2 = ticket_counter()  # New, independent counter
print(counter2())  # Ticket #1 (separate from counter1)