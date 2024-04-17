import validations

def load_lands_from_file(filename):
    lands = []
    try:
        with open(filename, "r") as file:
            for line in file:
                data = line.split(',')
                if validations.validate_land_data(data):
                    available_status = data[5].lower()
                    land = {
                        "id": int(data[0]),
                        "city": data[1],
                        "direction": data[2],
                        "anna": int(data[3]),
                        "price": int(data[4]),
                        "available": available_status.startswith(' available')
                    }
                    lands.append(land)
    except FileNotFoundError:
        print(f"Error: {filename} file not found.")
    return lands
