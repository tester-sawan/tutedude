# def sum(a,b,c=10):
#     result = a+b+c
#     return result
# output = sum(10,20) # Optional Argument.
# print(output)
# output = sum(20,10,20)
# print(output)
# If we input more argument than the defined parameter, then this will returns compile time error.
# To overcome this we have a provision of *args known as variable length, positional argument. It store the argument value as a 'Tuple'
def calculation(*greet):
    result1 =sum(greet)
    print(greet)
    return result1
result = calculation(1,2,3,4)
print(result)