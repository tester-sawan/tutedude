# How to declare a class in python
# Syntax: class <class_name>
class calculator:
    num =100 # Class Variable
# When the function is used in a class is called a method.
    def getData(self):
        print("I am executing a method in a class.")
# Creating object
obj = calculator()
# How to call the method of a class
obj.getData()
# How to call a variable of a class
print(obj.num)

