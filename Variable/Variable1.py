# Variable is like a container that store values.
# Since, python is a dynamic type language, it will automatically declare the data type as per the input data.
age = 25
name = "Sawan Kumar"
print(type(age))
print(age) #We can print the value by referring the variable name.
print(name)
# Type casting - changing the data type manually. 1. Implicit (automatic) 2. Explicit(manually)
# Explicit type casting
# syntax - <datatype>(<variable_name>)
age = str(25)
# type() function is used to find out the current data type of a variable or value.
print(type(age)) # This will print the type of the data type.
# Rule for declaring a variable
"""
1. Variable name should be start with the letter or underscore(_)
2. Variable name should not start with any number 
3. Variable name should contains letter, number & underscore
4. Variable name should not use any reserved keywords.
5. Variable name is a case-sensitive language.
"""
# Method of writing variable name
# 1. Camel Case(myVariableName) , 2. Pascel Case (MyVariableName) , 3. Snake case (my_variable_name)