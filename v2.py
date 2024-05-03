import math

# Calculation function
class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self, *args):
        raise NotImplementedError

    def calculate_perimeter(self, *args):
        raise NotImplementedError

    def display_info(self, area, perimeter, *dims):
        print(f"The area of a {self.name} with dimensions {', '.join(str(dim) for dim in dims)} is {area:.2f} and the perimeter is {perimeter:.2f}")
        return

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3, height=None):
        super().__init__("Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.height = height

    def calculate_area(self):
        if not self.height:
            raise ValueError("Height is required to calculate the area of a triangle.")
        return 0.5 * self.side1 * self.height

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

class Parallelogram(Shape):
    def __init__(self, base, height, side1, side2):
        super().__init__("Parallelogram")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def calculate_area(self):
        return self.base * self.height

    def calculate_perimeter(self):
        return 2 * (self.side1 + self.side2)