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