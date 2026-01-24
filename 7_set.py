"""
Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements.
Sets are defined by enclosing elements in curly braces {} or by using the built-in set() function.
Since sets are unordered, the items have no defined order, and you cannot access items using an index.
Sets are commonly used for membership testing, removing duplicates from a sequence, and performing mathematical operations 
like union, intersection, difference, and symmetric difference."""

s1 = {10, 20, 30, 40, 50, 10, 30}  # duplicate elements will be ignored
print("Set s1 (duplicates ignored):", s1)
s2 = set([60, 70, 80, 90, 100])  # creating a set from a list
print("Set s2 created from list:", s2)

# Adding elements to a set
s1.add(60)
print("Set s1 after adding 60. Position of 60 is random, as set is unordered:", s1)
s1.update(["Hello", "World"])  # adding multiple elements
print("Set s1 after adding 'Hello' and 'World':", s1)
s1.remove("Hello")
s1.remove("World")

# Removing elements from a set
s1.remove(20)  # raises KeyError if element not found
print("Set s1 after removing 20:", s1)
#s1.remove("Hello")  # This will raise a KeyError since "Hello" is not in the set
s1.discard("Hello")  # does not raise an error if element not found
print("Set s1 after discarding 'Hello' (not present):", s1)

# indexing, slicing and repetition are not supported in sets, because they are unordered
#print(s1.index(30))  # This will raise an AttributeError
#print(s1[0])        # This will raise a TypeError
#print(s1 * 3)      # This will raise a TypeError


# Set operations
print("Sets s1:", s1, " | s2:", s2)
s3 = s1.union(s2)
print("Union of s1 and s2 (s3):", s3)
s4 = s1.intersection(s2)
print("Intersection of s1 and s2 (s4):", s4)
s5 = s1.difference(s2)
print("Difference of s1 and s2 (s5):", s5)  # elements in s1 but not in s2
s6 = s1.symmetric_difference(s2)
print("Symmetric difference of s1 and s2 (s6):", s6)  # elements in either s1 or s2 but not in both

# frozen set - immutable version of set
fs1 = frozenset([1, 2, 3, 4, 5])
print("Frozen set fs1:", fs1)

# Trying to add or remove elements from frozen set will raise an AttributeError
#fs1.add(6)        # This will raise an AttributeError
#fs1.remove(2)     # This will raise an AttributeError
#fs1.discard(3)    # This will raise an AttributeError
print("Type of fs1:", type(fs1))