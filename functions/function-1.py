# Simple function with parameter.
def greeting_someone():
    print("Good morning everyone.")
    print('Have a pleasant day.')
#greeting_someone() # To call a function, we need to call with the function name.
# Function with a parameter.
def greet(name):
    print(f"Hey {name}, Welcome to Python Learning Course.")
# greet("Sawan Kumar")
# greet("Harsh Gautam")
# greet("Lakshay")
#Function  to check whether any number is even or odd.
def even_odd(num):
    if num%2==0:
        print(f"The number {num} is an Even Number.")
    else:
        print(f"The number {num} is an Odd Number.")
even_odd(3)
# Function with two parameter
def add(num1,num2):
    result = num1+num2
    print(f"Result is:{result}")
add(10,20)