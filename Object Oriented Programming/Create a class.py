# Creating a class
class MyClass:
    """
    This shows the documentation i.e doc string of a class. We can call this using help() function by passing 'class_name' as argument.
    """
    pass
# Creating an object
obj1 = MyClass() # Object has been created using the class_name
obj2 = MyClass()
# Obj1 and Obj2 are the object of the MyClass()
l1 = [10,20,30]
print(type(l1))
print(type(obj1))
print(type(obj2))
l1.append(40)
print(l1)
# Calling methods using object name > using .(dot)
#object_name . method_name()
print(help(MyClass))