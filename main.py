import time # imports time module  
import math # imports math module

print("Hello! user\n")
time.sleep(1) 
print("Welcome to my program.\n")
time.sleep(1)
def instructions(): # shows the instructions
    while True:
        show_instructions = input("Do you want to see the instructions? (Yes / No): ") # asks the user if they want to see the instructions
        
        FL = show_instructions[0].lower() 
        
        if show_instructions == '' or not FL in['y', 'n']: # functions for yes or no
            print("Please either enter a (Y)es or (N)o\n")
            return instructions() # returns to the top if they haven't enter thats required
        
        if FL == 'y': # prints out the instructions
            print("For this program you need to enter any")
            time.sleep(1)
            print("Shape")
            time.sleep(1)
            print("Dimensions")
            time.sleep(1)
            print("Area")
            time.sleep(1)
            print("and lastly the Perimeter")
            pass
        elif FL == 'n': # ignores the instructions and continues the program
            pass


class Shape: 
    def __init__(self, name):
        self.name = name

    def calculate_area(self, *args): # functions for calculating the area of a shape
        raise NotImplementedError

    def calculate_perimeter(self, *args): # functions for calculating the perimeter
        raise NotImplementedError

    def display_info(self, area, perimeter, *dims): # functions for displaying the answer
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

def get_user_input():
    shape = input("Please enter one of the chosen shapes\n 'Rectangle',\n 'Circle',\n 'Triangle',\n 'Parallelogram': ")
    
    if shape.capitalize() == "Rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        return Rectangle(length, width)
    
    elif shape.capitalize() == "Circle":
        radius = float(input("Enter the radius: "))
        return Circle(radius)
    
    elif shape.capitalize() == "Triangle":
        side1 = float(input("Enter the first side: "))
        side2 = float(input("Enter the second side: "))
        side3 = float(input("Enter the third side: "))
        height = float(input("Enter the height: "))
        return Triangle(side1, side2, side3, height)
    
    
    elif shape.capitalize() == "Parallelogram":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        side1 = float(input("Enter the first side: "))
        side2 = float(input("Enter the second side: "))
        return Parallelogram(base, height, side1, side2)
    
    else:
        raise ValueError("Please enter one of the chosen shapes")

def display_calculation_history(history):
    print("\nCalculation History:")
    for i, (shape, *dims) in enumerate(history, start=1): 
        area = shape.calculate_area()
        perimeter = shape.calculate_perimeter()
        shape.display_info(area, perimeter, *dims)

history = []
while True:
    try:
        shape = get_user_input()
        history.append((shape,))
        display_calculation_history(history)
    except ValueError as ve:
        print(ve)
        continue