# Inheritance in python allows a child class to use the methods & properties that are defined in base or parent class.
# Syntax for inheritance of a parent class into child class
# class <child_class_name>(parent_class_name):
from constructor import Calculator

class child1(Calculator):
    num2 = 200
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c
    def getCompleteData(self):
        return self.c + self.a + self.b
obj1 = child1(10,20,30)
print(obj1.getCompleteData())
print(child1.num1)
print(obj1.add())

# Class Variable will be called using the class name
# Instance variable will be called using the object name