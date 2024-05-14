def get_user_input():
    shape_name = input("Please enter one of the chosen shapes (or '(q)uit' to exit):\n 'Rectangle',\n 'Circle',\n 'Triangle',\n 'Parallelogram': ")
    if shape_name.lower() == 'q':
        print("Goodbye!")
        exit()

    shape_classes = {
        'Rectangle': Rectangle,
        'Circle': Circle,
        'Triangle': Triangle,
        'Parallelogram': Parallelogram
    }

    if shape_name.capitalize() not in shape_classes:
        raise ValueError(f"Invalid shape: {shape_name}. Please enter one of the chosen shapes.")

    shape_class = shape_classes[shape_name.capitalize()]

    if shape_class == Rectangle:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        return shape_class(length, width)
    elif shape_class == Circle:
        radius = float(input("Enter the radius: "))
        return shape_class(radius)
    elif shape_class == Triangle:
        side1 = float(input("Enter the first side: "))
        side2 = float(input("Enter the second side: "))
        side3 = float(input("Enter the third side: "))
        height = float(input("Enter the height: "))
        return shape_class(side1, side2, side3, height)
    elif shape_class == Parallelogram:
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        side1 = float(input("Enter the first side: "))
        side2 = float(input("Enter the second side: "))
        return shape_class(base, height, side1, side2)