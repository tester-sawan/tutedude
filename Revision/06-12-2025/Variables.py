# Variables are the container used to store data in it.
# Global Variable - Can be used Inside & Outside of a function.
import keyword
name = "Sawan Kumar"
def greet():
    global name # global keyword is used to modify the global variable under a function
    name = "Harsh"
    print(f"Hi {name}! Happy New Year.")
greet()
print(name)
# Local Variable - Scope of these variable are upto defined function.
#language = "Python programming language"
def course():
    language = "Java Programming language"
   # print(language)
    return  language
#course()
print("The local variable is: ", course())
# Non Local Variable - Those type of variable which are used in the nested function is called non-local variable.
def student_data():
    student_name = "Sawan Kumar"
    goal= "Software Development in Test"
    def show_data():
        print(student_name , goal, sep="-")
    show_data() # Call Inner Function
student_data() # Call Outer Function
print(keyword.kwlist)# It will return list having all reserved keyword..


