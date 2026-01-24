""" 
A tuple is an immutable collection type. It has same properties as list, but once created, its elements cannot be modified, added, or removed.
Tuples are defined by enclosing elements in parentheses () instead of square brackets [] used for lists. A tuple can be used as a key in a dictionary, 
whereas a list cannot, because tuples are immutable and hashable, while lists are mutable and unhashable. Typically, tuples are used to group related 
data together that should not change throughout the program.
"""
#declaration of tuple
t1 = (10, 20, 30, 40, 50)
print("Tuple t1:", t1)

#another way to declare tuple. However [] is a must to declare a list
t2 = 60, 70, 80, 90, 100
print("Tuple t2:", t2)

#a single element tuple
t3 = 10, # comma is necessary to define single element tuple. Without comma, it will be considered as single value (numeric or string), not a tuple
print("Single element tuple t3:", t3)

#print type
print("Type of t1:", type(t1))

#Putting a value into the tuple causes error
#t1[0] = 15 # This will raise a TypeError saying 'tuple' object does not support item assignment

#All list functions that do not modify the list can be used with tuples

#Convert a list into a tuple
l1 = [1, 2, 3, 4, 5]
t4 = tuple(l1)
print("Tuple t4 converted from list l1:", t4, type(t4))

