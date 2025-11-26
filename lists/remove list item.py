#1. remove() - Use to remove the specified element of a list.
studentinfo=["Sawan kumar","QA",4082,"Noida,Uttar Pradesh,India",True]
# remove 4082 from the studentinfo list.
studentinfo.remove(4082)
print(studentinfo)
#2. pop() - Use this method to remove the element based on index position and return the delete item
_deleteElement = studentinfo.pop(2)
print(studentinfo)
print("The deleted element from the list is: ",_deleteElement)
#3. clear() - This method is used to clear all element in a list.
studentinfo.clear()
print(studentinfo)