import math

# Calculation function
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
   
class Rectangle(Shape): # Calculates the area of the shape Rectangle
    def calculate_area(length, width):
        return length * width

    def calculate_perimeter(length, width): # Calculates the perimeter of the shape Rectangle
        return 2 * (length + width)
    
class Circle(Shape): # Calculates the area of the shape circle
    def calculate_area(self, radius):
        return math.pi * (radius ** 2)
    
    def calcualte_perimeter(self, radius): # Calculates the perimeter of the shape Circle
        return 2 * math.pi * radius

class Triangle(Shape): # Calculates the area of the shape Triangle
    def calculate_area(self, base, height):
        return 0.5 * base * height
    
    def calculate_perimeter(self, side1, side2, side3): # Calculates the perimeter of the shape Triangle
        return side1 * side2 * side3

class Parallelogram(Shape): # Calculates the area of the shape Parallelogram
    def calculate_area(self, base, height):
        return base * height
    
    def calculate_perimeter(self, side1, side2, side3, side4): # Calculates the perimeter of the shape Parallelogram
        return side1 * side2 * side3 * side4