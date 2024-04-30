def display_calculation_history():
    print("\nCalculation History:")
    for i, (shape, dim1, dim2, *extra_dims), in enumerate(history, start = 1):
        area, perimeter = shape.calculate_area(dim1, dim2, *extra_dims), shape.calculate_perimeter(dim1, dim2, *extra_dims)
        print("{}, {} with dimensions {} and {} {} : {:.2f} and {:.2f}".format(i, shape.name, dim1, dim2, ', and '.join('{}' for _ in extra_dims), *extra_dims, area, perimeter))