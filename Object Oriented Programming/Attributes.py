class Student:
    pass
student1 = Student()
student2 = Student()
# Assigning the instance variable into the object directly.
student1.name = "Sawan Kumar"
student1.roll = 88
print(student1.name)
print(student1.roll)
# Check the dunder of this class
print(student1.__dict__) # shows the dictionary that stores instance variable for object student1
print(help(Student))
print(student2.__dict__) # Shows empty dictionary.
