# 5. Remove the key "age" from the dictionary.
student = {"name":"Sawan","age":29,"grade":"A"}
# Method 1:
# del student["age"]
# print(student)
# Method 2:
deleted_value = student.pop("age")
print(student, "The deleted value is:",deleted_value)
# Method 3:
# deleted_value = student.popitem() # removed the last key: value pair in a dictionary.
# print(student,deleted_value)