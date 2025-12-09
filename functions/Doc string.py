# It is used to define the work flow of a function and can be access using help()
def greet_new_user(name, course, commencement_date):
    """
    This function will take these argument as:
    :name - Name of the candidate
    :course - Python Programming language
    :commencement_date: Date of enroll
    :return: None
    : This will print the greeting message on call.
    """
    print(f"Welcome {name}. Thank you for selecting {course}\nYour Course commencement date is: {commencement_date}.")
help(greet_new_user) # this will display the doc string message into the console.
greet_new_user("Sawan Kumar","Python Programming Language", "09-12-2025")
