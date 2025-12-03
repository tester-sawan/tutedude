# For loop in case of String
s1= "Sawan Kumar"
for char in s1:
    print(char)
print("Program ended.")
# For loop in dict
employee_info = {"Name":"Sawan Kumar", "Designation":"QA","Employee Id":4082}
#print(type(employee_info),employee_info)
for info in employee_info:
    print(f"{info}:{employee_info[info]}")