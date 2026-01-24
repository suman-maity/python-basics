# Collections in Python are List, Set and Dictionary

l1 = [10, 20.5, "Hello World", 40, 50] # list allows mixed data types
print("List l1:", l1)

#indexing
print("First element:", l1[0]) # first element
print("Third element:", l1[2]) # third element

#slicing
print("Elements from index 1 to 3:", l1[1:4]) # elements from index 1 to 3

#repitition
print("Repetition of list:", l1 * 2) # repeat list 2 times

#length of list
print("Length of list:", len(l1))

#modifying list
l1[2] = "Python Programming" # changing third element
print("Modified list:", l1)

#appending elements
l1.append(60) # appending an element at the end of the list
print("List after appending 60:", l1)

#inserting elements
l1.insert(1, 15) # inserting 15 at index 1
print("List after inserting 15 at index 1:", l1)

#removing elements
l1.remove(40) # removing element with value 40
print("List after removing 40:", l1)

#removing element that does not exist
# l1.remove(100) # This will raise a ValueError saying 100 not found in list

#popping elements
popped_element = l1.pop() # removes and returns the last element
print("Popped element:", popped_element)
print("List after popping:", l1)

#popping element at specific index
popped_element_index_2 = l1.pop(2) # removes and returns element at index 2
print("Popped element at index 2:", popped_element_index_2)
print("List after popping element at index 2:", l1)

#deleting elements using del
del l1[0] # deletes element at index 0
print("List after deleting element at index 0:", l1)

#another way to delete elements using del
#del l1[1:3] # deletes elements from index 1 to 2

#one more way to use del
#del(l1[1])

#delete entire list
#del l1
#print("List after deleting entire list:", l1) # This will raise a NameError since l1 is deleted

l1.clear() # clears all elements from the list
print("List after clearing all elements:", l1)

l1 = [10, 20.5, "Hello World", 40, 50] # re-initialize list
#print(max[l1]) #returns error as list contains mixed data types

l1.remove("Hello World") # removing string to have only numeric data types
print(max(l1)) # returns maximum value
print(min(l1)) # returns minimum value

#sorting a list. Default is ascending order
print(l1.sort())
print("Sorted list in ascending order:", l1)

#Reverse sorting a list
l1.sort(reverse=True)
print("Sorted list in descending order:", l1)



