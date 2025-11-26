#1. By the help of indexing
studentinfo=["Sawan kumar","QA",4082,"Noida,Uttar Pradesh,India",True]
print(studentinfo[0])
#2. By the help of negative indexing
print(studentinfo[-1]) # denotes the last element in the list.
#3. By the help of Range of Indexes
print(studentinfo[0:3]) # Retuns list of element from index position 0 to 2.
#3.1. Return list of element from index position 2 to last index value.
print(studentinfo[2:])
#3.2 Return list of element using negative indexing
print(studentinfo[-1:-5])
#3.3. Reverse the list element
print(studentinfo[::-1])
#4. Check if the item is present in the list
if 4082 in studentinfo:
    print("Item is present in the list.")
else:
    print("Item is not present in the list.")