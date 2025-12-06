name = "Sawan Kumar" # String in python is a sequence of characters enclosed with single or double quoted.
first_name = "Sawan"
last_name = "Kumar"
print(name)
#Indexing - It is a process of selecting a single character or element from a sequence of characters.
# Get the first character of string under name variable.
print(name[0])# It will return the first character
# Get the last character from a string.
print(name[-1]) # This will return the last character.
print(name[len(name)-1])
# Get the index position of w in "Sawan Kumar"
print(name.index("w"))# This will return the index no.
# String Concatenation - + Addition Operator
print(first_name+" "+last_name)
# We can find out the length of the string using len() function.
print(len(name))
# We can repeat a perticular string using *
print(first_name*3)
# Slicing a string - getting the sub string
print(name[:3])
# Membership - in or not in
print("n" in name)
print("t" not in name)



