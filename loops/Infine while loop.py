correct_password = "sawan"
incorrect_count = 0
while True:
    input_password = input("Enter your password to login your account: ")
    if incorrect_count==3:
        print("Permissible limit has been exceed. Kindly contact your system adminsitrator.")
        break

    elif input_password == correct_password and incorrect_count<=3:
        print("Successfully Log in")
        break
    elif input_password!=correct_password and incorrect_count<2:
        incorrect_count+=1
        print("Incorrect Password!! Please try again")
        continue
    else:
        print(f"Permissible limit exceed. Contact your system administrator.")
        break