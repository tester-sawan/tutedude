# Constructor is a method which has been executed automatically once an object of a class has been created.
# self keyword must be defined into a method in a class.
class Calculator:
    num1 = 100
# Create a constructor in python - __init__ is a keyword which are used to create a constructor in python.
    def __init__(self, a, b):
        self.a = a # Instance variable - variable defined inside a class-method
        self.b = b # Instance variable
        print("I am called automatically when object is created.")
    def greet(self):
        print("Welcome to Object Oriented Programming - Constructor")
    def add(self):
        # num1 = int(input("Enter the first number: "))
        # num2 = int(input("Enter the second number: "))
        result = self.a + self.b
        return result
# obj1 = Calculator(10,20) # as object is created, value defined in the argument will be auto-assigned with the parameter deifined in the constructor.
# obj2 = Calculator(20,30)
# obj1.greet()
# result1 = obj1.add()
# print(result1)
# print(obj2.add())