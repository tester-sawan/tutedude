#1. By using index number
studentinfo=["Sawan kumar","QA",4082,"Noida,Uttar Pradesh,India",True]
studentinfo[0] = "Harsh Gautam"
print(studentinfo)
#2. By using range to change the multiple value
studentinfo[1:3]="QA-1",4083
print(studentinfo)
#3. Replacing an index position by multiple values
studentinfo[0:1] = ["Atul Singh","Sawan Kumar"]
print(studentinfo)
#4. Insert the new element at the defined index position with removing the other element in the list.
studentinfo.insert(0,"Harsh Gautam")
print(studentinfo)