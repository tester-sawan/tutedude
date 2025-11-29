student_info = {"name":"Sawan Kumar", "designation":"QA Engineer","company":"Adventus.io","mobile no.":7044321721}
#1. pop() method - returns the deleted key value.
deletedKeys = student_info.pop("mobile no.")
print(f" {deletedKeys} has been deleted properly and the updated list is {student_info}")
#2. popitem() methods - Removed and returns the last key - value pair
print(student_info.popitem())
#3. del keyword
del student_info["name"]
print(student_info)
#4. clear() - empties the dictionaries.
student_info.clear()
print(student_info)
