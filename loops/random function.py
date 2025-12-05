# random module provide some important functions which are used to generate random numbers.
# To access random module, we need to import ramdom module.
import random
print(f"The random generated number is: {random.random()}") # This will return a random float number from 0.0 to 1.0
# Print the random interger number from a specific range
print(f"The random generated number from range 1 to 10 is: {random.randint(1, 10)}")
# Print the random number using the range function
print(f"The random generated number using a range is: {random.randrange(10, 20, 2)}")
# Print a random number from a list
employee_list = ["Sawan Kumar", "Harsh Gautam","Lakshay Khanna","Sabir"]
print(f"The random employee selected is: {random.choice(employee_list)}")
# Suffle a complete list with random function.
random.shuffle(employee_list) # This will suffle and change the order of the actual list.
print(f"{employee_list}")

