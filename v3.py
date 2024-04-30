# This function gets the user input to calculate their chosen shapes
def get_user_input(): 
    shape = input("Please enter one of the chosen shapes 'Rectangle', 'Circle', 'Triangle', 'Parallelogram': ")
    
    if shape.capitalize() == "Rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the length: "))
        return Rectangle ("rectangle"), length, width
    
    elif shape.capitalize() == "Circle":
        radius = float(input("Enter the radius: "))
        return Circle ("circle"), radius
    
    elif shape.capitalize() == "Triangle":
        side1 = float(input("Enter the first side: "))
        side2 = float(input("Enter the second side: "))
        side3 = float(input("Enter the third side: "))
        return Triangle ("triangle"), side1, side2, side3
    
    elif shape.capitalize() == "Parallelgram":
        side1 = float(input("Enter the first side: "))
        side2 = float(input("Enter the second side: "))
        side3 = float(input("Enter the third side: "))
        side4 = float(input("Enter the fourth side: "))
        return Parallelogram ("parallelogram"), side1, side2, side3, side4
    else:
        raise ValueError("Please enter one of the chosen shapes")
        return get_user_input

get_user_input()