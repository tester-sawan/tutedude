# List is a type of data structure which are used to store multiple values with different data type with duplicate items and it is also mutable.
#Creation of lists
#1. Using Square bracket
fruit = ["apple","banana","grapes","orange"]
studentinfo=["Sawan kumar","QA",4082,"Noida,Uttar Pradesh,India",True]
#Print the complete list
print(fruit)
print(studentinfo)
#Since list are mutable, we can edit,remove or add data with the help of index number.
#Retrive data from a list with index number.
#print(f"The value at the zero index position in the list i.e. fruit is: {fruit[0]}")
#Take the user input to find out the item as per search index number.
index = int(input("Enter the index number for which value is to be retrive: "))
print(f"The value at the {index} index position in the list i.e. fruit is: {fruit[index]}")
#Length of the list will be find by using len() function
print("The length of the list i.e fruit is: ",len(fruit))
#Find out the data type of a list
print(type(studentinfo))
#2. List can also created by using list()constructor.
car_list = list(("Maruti","BMW","Honda","KIA","Morris"))
print(car_list)