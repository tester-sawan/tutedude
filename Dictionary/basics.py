# Dictionaries are one of the build-in data type in python that are used to store multiple data in one variable. It is mutable in nature.
# Dictionaries does not store duplicate values.
# How to define dictionary in python.
student_info = {"name":"Sawan Kumar", "designation":"QA Engineer","company":"Adventus.io","mobile no.":7044321721}
print(f"The data type of a variable - student_info is {type(student_info)} . {student_info}")
# How to retrieve the value of any key from the dictionary.
# Let take a user input.
# search_key = input("Enter the key name to find out its value: ")
# print(f"The value of the {search_key} is : {student_info[search_key]}")
# Duplicate key is not allowed.
# How to find out the length of the dictionary. Use len() function.
print(f"The total no of key available in student_info is: {len(student_info)}")
# A dictionary can also hold another dictionary or list.
student_info1 = {"name":"Sawan Kumar", "designation":"QA Engineer","Work days":["MON","TUE","WED","THR","FRI"],"Leave type":{"CL":1,"SL":1,"AL":2}}
print(student_info1["Work days"][1], student_info1["Leave type"]["CL"])
