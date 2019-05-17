# Stacks are a container of objects that are inserted and removed according to the
# Last-In-First_Out (LIFO) concept.
# Stacks can be implemented using lists in Python.
# When elements are added to a stack it is known as a push operation, whereas when you
# remove or delete an element it is called a pop operation.

# Bottom -> 1 -> 2 -> 3 -> 4 -> 5 (Top)
stack = [1,2,3,4,5]
stack.append(6) # Bottom -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 (Top)
print(stack)

stack.pop() # Bottom -> 1 -> 2 -> 3 -> 4 -> 5 (Top)
stack.pop() # Bottom -> 1 -> 2 -> 3 -> 4 (Top)
print(stack)