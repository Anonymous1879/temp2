import datetime

def update_lands_in_file(filename, lands):
    try:
        with open(filename, "w") as file:
            for land in lands:
                id_str = str(land['id'])
                city_str = land['city'][1:]  # Remove the first character from city
                direction_str = land['direction'][1:]  # Remove the first character from direction
                anna_str = str(land['anna'])
                price_str = str(land['price'])
                available_str = "Available" if land['available'] else "Not Available"
                file.write(id_str + ", " + city_str + ", " + direction_str + ", " + anna_str + ", " + price_str + ", " + available_str + "\n")
    except Exception as e:
        print("Error occurred while writing land data:", e)



def generate_timestamp():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    return timestamp
