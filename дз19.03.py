# task 1
class Soda:
    def __init__(self, taste=None):
        if isinstance(taste, str) and taste.isalpha():
            self.taste = taste
        else:
            self.taste = None

    def taste_soda(self):
        if self.taste:
            return f"У вас газировка с {self.taste} вкусом"
        return "У вас обычная газировка"


user_input = input("What taste does your soda have? ")
if user_input and not user_input.isalpha():
    print("Ошибка: введите вкус буквами")
else:
    soda_taste = Soda(user_input)
    print(soda_taste.taste_soda())


# task 2
class Math:
    def __init__(self, x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x = x
            self.y = y
        else:
            self.x = None
            self.y = None

    def addition(self):
        if self.x is not None and self.y is not None:
            return self.x + self.y
        return "Error: enter incorrect data"

    def subtraction(self):
        if self.x is not None and self.y is not None:
            return self.x - self.y
        return "Error: enter incorrect data"

    def multiplication(self):
        if self.x is not None and self.y is not None:
            return self.x * self.y
        return "Error: enter incorrect data"

    def division(self):
        if self.x is not None and self.y is not None:
            return self.x / self.y
        return "Error: enter incorrect data"


def get_number_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Enter only numbers!")


x_input = get_number_input("What is the first number? ")
y_input = get_number_input("What is the second number? ")

my_math = Math(x_input, y_input)
print(f"Addition: {my_math.addition()}")
print(f"Subtraction: {round(my_math.subtraction(), 4)}")
print(f"Multiplication: {my_math.multiplication()}")
print(f"Division: {round(my_math.division(), 4)}")
