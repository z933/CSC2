import time  # imports time module
import math  # imports math module

print("Hello! user\n")
time.sleep(0.5)
print("Welcome to my program.\n")
time.sleep(0.5)


def instructions():  # shows the instructions
    while True:
        show_instructions = input("Do you want to see the instructions? (Yes / No): ")  # asks the user if they want to see the instructions

        FL = show_instructions[0].lower()

        if show_instructions == '' or FL not in ['y', 'n']:  # functions for yes or no
            print("Please either enter a (Y)es or (N)o\n")
            continue  # continues the loop to prompt the user again

        if FL == 'y':  # prints out the instructions
            print("For this program you need to enter any")
            time.sleep(0.1)
            print("Shape")
            time.sleep(0.1)
            print("Dimensions")
            time.sleep(0.1)
            print("Area")
            time.sleep(0.1)
            print("and lastly the Perimeter")
            time.sleep(0.1)
            print("you can also enter q to quit the program")
            break  # breaks out of the loop as instructions are displayed
        elif FL == 'n':  # ignores the instructions and continues the program
            break  # breaks out of the loop as instructions are not needed


instructions()  # Call the instructions function


class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self, *args):  # functions for calculating the area of a shape
        raise NotImplementedError

    def calculate_perimeter(self, *args):  # functions for calculating the perimeter
        raise NotImplementedError

    def display_info(self, area, perimeter, *dims):  # functions for displaying the answer
        print(f"The area of a {self.name} with dimensions {', '.join(str(dim) for dim in dims)} is {area:.2f} and the perimeter is {perimeter:.2f}")
        return


class Rectangle(Shape): # calculator function for the shape rectangle
    def __init__(self, length, width): 
        super().__init__("Rectangle") 
        self.length = length 
        self.width = width

    def calculate_area(self): # calculates the area of the rectangle once the user enters the length and width value
        return self.length * self.width

    def calculate_perimeter(self): # calculates the perimeter of the rectangle once the user enters the length and width value
        return 2 * (self.length + self.width)


class Circle(Shape): # calculator function for the shape Circle
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self): # calculates the area of the circle once the user enters the radius value
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self): # calculates the perimeter of the circle once the user enters the radius value
        return 2 * math.pi * self.radius


class Triangle(Shape): # calculator function for the shape Triangle
    def __init__(self, side1, side2, side3, height=None):
        super().__init__("Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.height = height

    def calculate_area(self): # calculates the area of the triangle once the user enters the side1 and height value
        if not self.height:
            raise ValueError("Height is required to calculate the area of a triangle.")
        return 0.5 * self.side1 * self.height

    def calculate_perimeter(self): # calculates the perimeter of the triangle once the user enters the side1 side2 and side3 value
        return self.side1 + self.side2 + self.side3


class Parallelogram(Shape): # calculator function for the shape parallelogram
    def __init__(self, base, height, side1, side2):
        super().__init__("Parallelogram")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def calculate_area(self): # calculates the area of the parallelogram once the user enters the base and height value
        return self.base * self.height

    def calculate_perimeter(self): # calculates the perimeter of the parallelogram once the user enters the side1 and side2 value
        return 2 * (self.side1 + self.side2) 


def get_user_input(): # gets the user input
    shape_name = input(
        "Please enter one of the chosen shapes (or '(q)uit' to exit):\n 'Rectangle',\n 'Circle',\n 'Triangle',\n 'Parallelogram'\n=> ")
    if shape_name.lower() == 'q': # an exit function if the user dont want to use the program
        print("Goodbye!")
        exit()

    shape_classes = { 
        'Rectangle': Rectangle,
        'Circle': Circle,
        'Triangle': Triangle,
        'Parallelogram': Parallelogram
    }

    if shape_name.capitalize() not in shape_classes: # if the user had a typo the program prints this message and lets the user choose again without any error
        raise ValueError("Invalid shape: {}. Please enter one of the chosen shapes.".format(shape_name)) 

    shape_class = shape_classes[shape_name.capitalize()] 

    if shape_class == Rectangle: # input function for rectangle
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        return shape_class(length, width)
    elif shape_class == Circle: # input function for circle
        radius = float(input("Enter the radius: "))
        return shape_class(radius)
    elif shape_class == Triangle: # input function for triangle
        side1 = float(input("Enter the first side: "))
        side2 = float(input("Enter the second side: "))
        side3 = float(input("Enter the third side: "))
        height = float(input("Enter the height: "))
        return shape_class(side1, side2, side3, height)
    elif shape_class == Parallelogram: # input function for parallelogram
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        side1 = float(input("Enter the first side: "))
        side2 = float(input("Enter the second side: "))
        return shape_class(base, height, side1, side2)


def display_calculation_history(history): # shows the history of the the calculation
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
