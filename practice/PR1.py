import math


class FormulaCalculator:

    def calculate_formula(self, x):
        raise NotImplementedError

    def sum_with_for(self, start, end, step):
        results = []
        count = int((end - start) / step) + 1
        for i in range(count):
            x = start + i * step
            results.append(self.calculate_formula(x))
        return sum(results), results

    def sum_with_while(self, start, end, step):
        results = []
        x = start
        while x <= end + 1e-9:
            results.append(self.calculate_formula(x))
            x += step
        return sum(results), results

    def print_results(self, x_single, start, end, step):
        sum_for, array_for = self.sum_with_for(start, end, step)
        sum_while, array_while = self.sum_with_while(start, end, step)

        print(f"Результат при X = {x_single}: {self.calculate_formula(x_single):.5f}")
        print(f"Сумма (for): {sum_for:.5f}")
        print(f"Массив (for): {[round(num, 5) for num in array_for]}")
        print(f"Сумма (while): {sum_while:.5f}")
        print(f"Массив (while): {[round(num, 5) for num in array_while]}")


class Dog(FormulaCalculator):

    def __init__(self, breed, age, name):
        self.breed = breed
        self.age = age
        self.name = name

    def calculate_formula(self, x):
        return 1.1 * math.exp(x) + abs(math.cos(math.sqrt(math.pi * x))) - 4 / 9

    def show_info(self):
        print(f"Собака: {self.name}, Порода: {self.breed}, Возраст: {self.age}")


class Triangle(FormulaCalculator):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimeter(self):
        return self.a + self.b + self.c

    def calculate_area(self):
        p = self.calculate_perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def calculate_formula(self, x):
        numerator = math.log(math.log(math.sqrt(abs(x - 2)) + 1.2))
        denumerator = 2 + math.exp(x)
        cube = (2 / x) ** (1 / 3)
        return (numerator / denumerator) + cube

    def show_info(self):
        print(f"Периметр: {self.calculate_perimeter()}")
        print(f"Площадь: {self.calculate_area():.2f}")



# ___init_____ = ____main_____
my_dog = Dog(breed="Мопсы", age=33, name="Арчибальд")
my_triangle = Triangle(3, 4, 5)

x_target, x_start, x_end, x_step = 0.5, 0.1, 0.6, 0.1

my_dog.show_info()
my_dog.print_results(x_target, x_start, x_end, x_step)

print()

my_triangle.show_info()
my_triangle.print_results(x_target, x_start, x_end, x_step)
