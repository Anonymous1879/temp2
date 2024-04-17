def load_lands_from_file(filename):
    lands = []
    try:
        with open(filename, "r") as file:
            for line in file:
                data = line.split(',')
                if validate_land_data(data):
                    available_status = data[5].strip().lower()
                    land = {
                        "id": int(data[0]),
                        "city": data[1],
                        "direction": data[2],
                        "anna": int(data[3]),
                        "price": int(data[4]),
                        "available": available_status.startswith('available')
                    }
                    lands.append(land)
    except FileNotFoundError:
        print(f"Error: {filename} file not found.")
    return lands

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
        available_status = data[5].strip().lower()
        if available_status.startswith('available') or available_status.startswith('not available'):
            return True
        else:
            print("Invalid availability status.")
            return False
    except ValueError:
        print("Invalid land data values.")
        return False
