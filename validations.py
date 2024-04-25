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
        
def validate_late_duration(prompt):
    while True:
        late_duration_str = input(prompt)
        try:
            late_duration = int(late_duration_str)
            if late_duration >= 0:
                return late_duration
            else:
                print("Late duration must be a non-negative number.")
        except ValueError:
            if late_duration_str.isdigit():  # Negative number
                print("Late duration must be a non-negative number.")
            else:  # Non-numeric input
                print("Invalid input. Please enter a valid number.")

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

def validate_land_data(data):
    if len(data) != 6:
        print("Invalid land data format.")
        return False
    try:
        int(data[0])  # ID
        data[1]  # City
        data[2]  # Direction
        int(data[3])  # Anna
        int(data[4])  # Price
        available_status = data[5].lower()
        if available_status.startswith(' available') or available_status.startswith(' not available'):
            return True
        else:
            print("Invalid availability status.")
            return False
    except ValueError:
        print("Invalid land data values.")
        return False
