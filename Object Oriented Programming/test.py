class Company:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "Adventus.io")
        self.country = kwargs.get("country", "India")

Company()
Company(name="Amazon", country="USA")
#info = Company(name="Amazon", country="USA")
info = Company()
print(info.name)
print(info.country)
