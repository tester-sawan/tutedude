# 3. Add a new key "city" to the dictionary with any value.
student = {"name":"Sawan","age":29,"grade":"A"}
# # Method 1:
# student["city"]="Noida"
# print(student)
#Method 2:
student.update({"city":"Noida"})
print(student, type(student))
