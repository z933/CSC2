import time

print("Hello! user\n")
time.sleep(1)
print("Welcome to my program.\n")
time.sleep(1)
def instructions():
    while True:
        show_instructions = input("Do you want to see the instructions? (Yes / No): ")
        
        FL = show_instructions[0].lower()
        
        if show_instructions == '' or not FL in['y', 'n']:
            print("Please either enter a (Y)es or (N)o\n")
            return instructions()
        
        if FL == 'y':
            print("For this program you need to enter any")
            time.sleep(1)
            print("Shape")
            time.sleep(1)
            print("Dimensions")
            time.sleep(1)
            print("Area")
            time.sleep(1)
            print("and lastly the Perimeter")
        
        elif FL == 'n':
            pass
        
        print("pass")

instructions()