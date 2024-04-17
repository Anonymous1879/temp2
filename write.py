import datetime

def update_lands_in_file(filename, lands):
    try:
        with open(filename, "w") as file:
            for land in lands:
                availability = 'Available' if land["available"] else 'Not Available'
                file.write(f"{land['id']}, {land['city']}, {land['direction']}, {land['anna']}, {land['price']}, {availability}\n")
    except Exception as e:
        print(f"Error occurred while updating land data: {e}")

def generate_timestamp():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    return timestamp
