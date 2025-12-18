class Company:
    def __init__(self,name,address,city,state,country):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.country = country
    def greet(self,name):
        print(f"Hi, {name},Welcome to the Constructor Learning.")
    def contact_info(self):
        return f"{self.name},{self.address},{self.city},{self.state},{self.country}."
info1 = Company("Adventus.io","KS Corporate Tower","Noida","Uttar Pradesh","India")
info1.greet("Sawan Kumar")
print(info1.contact_info())