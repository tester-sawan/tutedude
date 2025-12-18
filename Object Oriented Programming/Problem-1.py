class BasicCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


obj1 = BasicCalculator(10, 5)
print(f"Addition: {obj1.addition()}")
print(f"Substraction: {obj1.subtraction()}")
print(f"Multiplication: {obj1.multiplication()}")
print(f"Division: {obj1.division()}")

