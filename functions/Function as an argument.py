# In Python,we can pass the function as an argument.
def double(number):
    result = number*2
    return result
def power(number):
    result = number**2
    return result
# Take a user input and calculate the power using double function as argument.
number = int(input("Enter a number: "))
output = power(double(number))
print(f"Result is: {output}.")