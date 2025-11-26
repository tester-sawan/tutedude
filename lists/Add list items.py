#1. Using append() - This method is used to add an element to the end in a list.
studentinfo=["Sawan kumar","QA",4082,"Noida,Uttar Pradesh,India",True]
fruit = ["apple","banana","grapes","orange"]
studentinfo.append("Adventus.io")
print(studentinfo)
#2. Using insert() - This method is used to add new value at defined index position.
studentinfo.insert(1,"QA-1")
print(studentinfo)
#3. Using extend() - This method is used to add new list inside the current list
studentinfo.extend(fruit)
print(studentinfo)