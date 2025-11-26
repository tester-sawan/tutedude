"""
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
Expected Output:
The program should output a greeting like:
"""
first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
full_name = first_name+" "+last_name
print(f"Hello, {full_name}! welcome to the python program.")
