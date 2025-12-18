# Constructors are the special method that are called automatically when object is created. It main role is to initialise the object by assigning the attributes.
# There are two type of constructor:
# 1. Default Constructor
# 2. Parameterised Constructor
# 1. Default Constructor
class Company:
    topic = "Object Oriented Programming"
    def __init__(self):
        self.company_name = "Adventus.io" #Instance Variable
        self.corporate_address = "KS Corporate Tower, Sector-16A, Noida Film City" #Instance Variable
        self.country = "India" #Instance Variable
    def company_info(self):
        print(f"{self.company_name},{self.corporate_address},{self.country}")

info1 = Company() # Instance variable data auto assigned.
print(info1.company_name) # Instance variable data will be called using object name.
print(info1.corporate_address,",",info1.country)
info1.company_info()

