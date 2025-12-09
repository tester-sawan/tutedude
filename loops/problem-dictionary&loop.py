"""
We have the following dictionary containing details:
user = {"user_name":"my_user",
        "password":"test@123",
        "email":"myuser@example.com",
        "address":"ABC Road, 123456",
        "Country":"Australia"}
Delete the sensitive information from the user dictionary present in a list
sensitive_info = ["password","address"]
"""
user = {"user_name":"my_user",
        "password":"test@123",
        "email":"myuser@example.com",
        "address":"ABC Road, 123456",
        "Country":"Australia"}
sensitive_info = ["password","address"]
#available_keys = user.keys()
#print(available_keys)
for key in sensitive_info:
   for j in list(user.keys()):
       if j==key:
           user.pop(j)
print(user)
