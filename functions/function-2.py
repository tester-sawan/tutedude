# Returning value from a function:
def odd_even(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
#print(result)
# Returning the result for addition  of two number
def add(num1,num2):
    result = num1+num2
    return result
result = add(10,6)
print(result)
# Input the argument with the user input.
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
# Write a function which returns multiple values.
def arithmeticOperation(num1,num2):
    add = num1+num2
    substract = num1-num2
    multiply = num1*num2
    return add,substract,multiply
# output = arithmeticOperation(num1,num2)
# print(output) # Retuns the values as an tuple.
# We can unpack it also:
add_result,sub_result,mul_result = arithmeticOperation(num1,num2)
print("Addition: ",add_result)
print("Substraction: ",sub_result)
print("Multiplication: ",mul_result)