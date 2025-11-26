# List operations - slicing, concat, repeat, append, insert
#1. Slicing if lists
number=[1,2,3,4,5,6,7,8]
#Length of the list
print(f"The total number of element found under 'number' list is: {len(number)}")
print(f"The elements from index position 1 to 5 available under list 'number' is: {number[1:6]}")
#slicing using negative indexing
print(number[-1:-5:-1])
#reverse the entire list
print(number[::-1])
#2. Concat of list
fruits = ["apple","manago","banana"]
concat_list = number+fruits
print(concat_list)
#3. repeat operations in list
print(number*3)
#4.Append "dragonfruit" under fruits list. - add the element name at the end of the list.
print(fruits.append("dragonfruit")) # It will return None.
fruits.append("dragonfruit")
print(fruits)
#insert> add the element under the specific index position
fruits.insert(1,"dragonfruits")
print(fruits)
