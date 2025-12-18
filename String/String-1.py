language = "Python Programming Language"
name = "Sawan is learning"
website = "www.adventus.io"
age = " twenty nine "
# Get the length of the string
print(len(language))
# Extract the second character available under the language variable.
print(language[1]) # as index starts from 0
# Get the first five character from language5
print(language[0:5])
# Get the last five character from language
print(language[(len(language)-5):(len(language)+1)])
# Get the reverse of the language
print(language[-1:-9:-1])
# Joining of two strings
print(name+" "+language)
# Membership i.e in or not in
print("is" in name) # Returns boolean value >> True
print("learning" not in name)# >> False
# Split method > used to split the string from the defined character as argument.
print(website.split(".")) # Returns a list
split_data = website.split(".")
for data in split_data:
    print(data)
# Print the 1 index of the splited data
print(split_data[1])
#How to get the index position of a charcater
print(language.index("n"))
# Find the index position of an element from a list
print(split_data.index("io"))
# Trim the data using strip() method
print(age)
#print(f"The trim value is {age.strip(" ")}")
print(age.lstrip(" "))
print(age.rstrip(" "))