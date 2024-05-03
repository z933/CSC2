history = []
while True:
    try:
        shape = get_user_input()
        history.append((shape,))
        display_calculation_history(history)
    except ValueError as ve:
        print(ve)
        continue