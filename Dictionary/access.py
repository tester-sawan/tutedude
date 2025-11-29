# There are some methods that are used to retrive the keys or Values from a dictionary.
#1. Using Square bracket with the key value
student_info = {"name":"Sawan Kumar", "designation":"QA Engineer","company":"Adventus.io","mobile no.":7044321721}
print(student_info)
print(student_info["name"]) # Returns the value of the associated key "name"
#2. Using the get() method
print(student_info.get("company"))
#3. keys() methods will return all keys available under given dictionary.
print(student_info.keys())
#4. values() methods will returns all values available under given dictionary.
print(student_info.values())
#5. items() methods will returned each element as a tuple in a list.
print(student_info.items())
# Check if the following keys is available in a dictionary - membership (in, not in)
if "designation" in student_info:
    print("This key is available under student_info dictionary.")
else:
    print("Sorry, this is an invalid key.")

