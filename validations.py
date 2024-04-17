def validate_name(prompt):
    while True:
        name = input(prompt)
        if not any(char.isdigit() for char in name):
            return name
        else:
            print("Name cannot contain numbers.")
            continue_choice = input("Do you want to enter your name again? (y/n): ").lower()
            if continue_choice != 'y':
                return None

def validate_duration(prompt):
    while True:
        try:
            duration = int(input(prompt))
            if duration > 0:
                return duration
            else:
                print("Duration must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return 0

def choose_land_id(lands, available=True):
    while True:
        try:
            land_id = int(input(f"Enter land ID (0 to stop): "))
            if land_id == 0:
                return 0
            land = next((land for land in lands if land["id"] == land_id and land["available"] == available), None)
            if land:
                return land_id
            else:
                print("Invalid land ID.")
                continue_choice = input("Do you want to enter ID again? (y/n): ").lower()
                if continue_choice != 'y':
                    return 0
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue_choice = input("Do you want to enter ID again? (y/n): ").lower()
            if continue_choice != 'y':
                return 0

def choose_option():
    while True:
        try:
            option = int(input("Enter your choice: "))
            if option in [1, 2, 3]:
                return option
            else:
                print("Option not available")
        except ValueError:
            print("Invalid input. Please enter a valid number.")