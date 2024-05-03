def display_calculation_history(history):
    print("\nCalculation History:")
    for i, (shape, *dims) in enumerate(history, start=1): 
        area = shape.calculate_area()
        perimeter = shape.calculate_perimeter()
        shape.display_info(area, perimeter, *dims)