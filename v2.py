import math

class Shape:
    def __init__(name, self):
        self.name = name

    def calculate_area(self, dim1, dim2):
        raise NotImplementedError
    
    def calculate_perimeter(self, dim1, dim2):
        raise NotImplementedError
    
    def display_info(self, area, perimeter):
        print("The area of a {} with dimensions {} and {} is {} and the perimeter is {}".format(self.name, dim1, dim2, area, perimeter))
        return

class Rectangle(Shape):
    def calculate_area(length, width):
        return length * width

    def calculate_perimeter(length, width):
        return 2 * (length + width)
    
class Circle(Shape):
    def calculate_area(self, radius):
        return math.pi * (radius ** 2)
    
    def calcualte_perimeter(self, radius): 
        return 2 * math.pi * radius

class Triangle(Shape):
    def calculate_area(self, base, height):
        return 0.5 * base * height
    
    def calculate_perimeter(self, side1, side2, side3):
        return side1 * side2 * side3

class Parallelogram(Shape):
    def calculate_area(self, base, height):
        return base * height
    
    def calculate_perimeter(self, side1, side2, side3, side4):
        return side1 * side2 * side3 * side4