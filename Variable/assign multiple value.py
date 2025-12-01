# We can assign multiple values to multiple variable or same value to many variable.
# Case-1 (Assigning multiple value to multiple variable)
a,b,c=10,20,30
print(a,b,c)
#Case-2 (Assign same value to multiple variable.)
a=b=c="Sawan"
print(a,b,c)
# Case-3 (Python also provide a feature to unpack a collection  to variable)
student_info1 = ["Sawan Kumar","QA Engineer",4082]
name,designation,employee_id = student_info1
print(name,designation,employee_id,sep="-")
# Global Variable
name1="sawan"
def newindo():
    name1 = "Harsh"
    print(name1)
newindo()
print(name1)