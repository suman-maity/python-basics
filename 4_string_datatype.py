s = "Hello, World!"
s1 = """ This is a multiline string example.
It can span multiple lines.
"""
print(s)
print(s1)

# indexing
print("Fourth character:", s[4]) # index starts at 0

#repitition
print("Repetition:", s * 3) # repeat string 3 times

# length of string
print("Length of string:", len(s))

print("\n")

#slicing
print("Substring (0-4):", s[0:5]) # from index 0 to 4
print("Substring (7-end):", s[7:]) # from index 7 to end
print("Substring (start-5):", s[:5]) # from start to index 4, last index is exclusive
print("Substring (start-end-step 2):", s[1:10:2]) # from 1st element to 9th element with step 2, i.e., every second character
print("Substring (start-end-step 2):", s[::2]) # from start to end with step 2, i.e., every second character

print("\n")

# negative indexing
print("Last character:", s[-1]) # last character. -1 represents last character
print("Second last character:", s[-2]) # second last character
print("Substring using negative indexing (-5 to end):", s[-5:]) # last 5 characters - from -5 index to end, this is printing from left to right
print("Substring using negative indexing (start to -5):", s[:-5]) # from start to -5 index, this is printing from left to right
print("Substring using negative indexing (-10 to -5):", s[-10:-5]) # from -10 index to -5 index, this is printing from left to right
print("Substring using negative indexing (start to end with step -1):", s[::-1]) # reverse the string, step is negative, means move from right to left
print("Slicing does not change original string:", s) # original string remains unchanged

print("\n")

#stripping whitespace
s2 = "   Hello, Python!    "
print("Original string with spaces:'" + s2 + "'")
print("After strip:'" + s2.strip() + "'") # removes leading and trailing whitespace
print("After lstrip:'" + s2.lstrip() + "'") # removes leading whitespace
print("After rstrip:'" + s2.rstrip() + "'") # removes trailing whitespace

print("\n")

#finding a substring
s3 = "The world is beautiful. The world is vast. World is amazing."
print("First occurrence of 'world' at index:", s3.find("world")) # returns index of first occurrence
print("First occurrence of 'World' at index:", s3.find("World")) # case-sensitive search
print("Case sensitive search - 'Vast' found at index:", s3.find("Vast")) # "Vast" not found, returns -1, because of case sensitivity
print("Find 'world' starting from index 10:", s3.find("world", 10)) # search starting from index 10
print("Find 'world' starting from index 10, ending at 12:", s3.find("world", 10, 12)) # search starting from index 10, ending at 12, not found, returns -1
print("slicing oper")

print("\n")

#count occurrences of a substring
print("Count of 'world':", s3.count("world")) # counts occurrences of substring
print("Count of 'World':", s3.count("World")) # case-sensitive count

print("\n")

#replace substring
print(s3.replace("world", "universe")) # replaces all occurrences

#change case
s4 = "Hello, Python!"
print("Original string:", s4)
print("Uppercase:", s4.upper())
print("Lowercase:", s4.lower())
print("Title Case:", s4.title())
print("Swap Case:", s4.swapcase())
print("Original string remains unchanged:", s4)