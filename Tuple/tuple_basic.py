#Tuple is a built-in data type which are used to store multiple values in a single variable. Tuple is a non-mutable in nature.
# How to create a tuple.
month_name = ("jan","feb","march","april","may","jun","july","aug","sept","oct","nov","dec")
print(type(month_name))# Returns the type of the variable.
# We can access the elements from a tuple
#1. With the help of positive indexing
print(month_name[1])# Returns the value from the index position 1
#2. With the help of negative indexing.
print(month_name[-1])# Returns the last element
#3. Slicing for getting the range value.
print(month_name[0:5])
print(month_name[-12:-7:2])
# len() function is used to find out the no. of element available in a tuple.
print(len(month_name)) # Returns the count.
# Create a tuple with only one element.
column_required = ("name",)
print(type(column_required))
# A tuple can store any data type
column_required1=("class-section",1,1.90,True)
print(type(column_required1))
print(column_required1)
#Tuple concatenate
column_required+=column_required1
print(column_required)
#Check if an item exists
print("class-section1" in column_required)# Returns boolean value