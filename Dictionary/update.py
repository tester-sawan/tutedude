# In this, we will see the available technique which is used for updating the existing dictionary.
#1. With the help of the key name.
student_info = {"name":"Sawan Kumar", "designation":"QA Engineer","company":"Adventus.io","mobile no.":7044321721}
student_info["name"]="Harsh Gautam"
print(student_info)
#2. update()
student_info.update({"designation": "Sr. QA"})
print(student_info)
