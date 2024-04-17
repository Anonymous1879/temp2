import validations
import read
import write
import datetime

def start():
    lands = read.load_lands_from_file("land_data.txt")
    
    while True:
        welcome_screen()
        choice = validations.choose_option()
        if choice == 1:
            display_lands(lands)
            rent_land(lands)
        elif choice == 2:
            display_lands(lands)
            return_land(lands)
        elif choice == 3:
            print("Exiting TechnoPropertyNepal...")
            break
        else:
            print("Invalid choice. Please try again.")

def welcome_screen():
    print("Welcome to TechnoPropertyNepal")
    print("1. Rent Land")
    print("2. Return Land")
    print("3. Exit")

def display_lands(lands):
    print("Available Lands:")
    print("+------+--------------+---------------------+------+--------+---------------+")
    print("|  ID  |     City     |      Direction      | Anna | Price  | Availability  |")
    print("+------+--------------+---------------------+------+--------+---------------+")
    for land in lands:
        print("| {:<4} | {:<12} | {:<19} | {:<4} | {:<6} | {:<13} |".format(land['id'], land['city'], land['direction'], land['anna'], land['price'], 'Available' if land['available'] else 'Not Available'))
    print("+------+--------------+---------------------+------+--------+---------------+")

def rent_land(lands):
    name = validations.validate_name("Enter your name: ")
    if name is None:
        return

    rented_lands = []
    total_amount = 0

    while True:
        land_id = validations.choose_land_id(lands, available=True)
        if land_id == 0:
            break

        land = next((land for land in lands if land["id"] == land_id), None)
        if land and land["available"]:
            duration = validations.validate_duration("Enter rental duration (months): ")
            if duration == 0:
                continue
            amount = land["price"] * duration
            total_amount += amount
            rented_lands.append({"id": land_id, "duration": duration, "amount": amount, "city": land["city"], "direction": land["direction"], "anna": land["anna"], "price": land["price"]})
            land["available"] = False
        else:
            print("Land is not available.")

    if rented_lands:
        write.update_lands_in_file("land_data.txt", lands)  # Update the file after renting
        timestamp = write.generate_timestamp()
        # Get the current date and time
        now = datetime.datetime.now()

        # Format the date and time
        formatted_date_time = now.strftime("%Y/%m/%d %H:%M:%S")

        invoice_name = f"{name}_rent_invoice_{timestamp}.txt"  # Add timestamp to invoice name
        with open(invoice_name, "w") as file:
            file.write("+---------------------------------------------------------------------------------+\n")
            file.write("|                               TechnoPropertyNepal                               |\n")
            file.write("+---------------------------------------------------------------------------------+\n")
            file.write("|                                                                                 |\n")
            file.write(f"|Rent Invoice for {name:<64}|\n")
            file.write(f"|Date: {formatted_date_time:<75}|\n")
            file.write("+------+--------------+---------------------+------+--------+----------+----------+\n")
            file.write("|  SN  |     ID       |        City         | Anna | Price  | Duration | Amount   |\n")
            file.write("+------+--------------+---------------------+------+--------+----------+----------+\n")
            sn = 1
            for rented_land in rented_lands:
                file.write("| {:<4} | {:<12} | {:<19} | {:<4} | {:<6} | {:<8} | {:<8} |\n".format(sn, rented_land['id'], rented_land['city'], rented_land['anna'], rented_land['price'], rented_land['duration'], rented_land['amount']))
                sn += 1
            file.write("+------+--------------+---------------------+------+--------+----------+----------+\n")
            file.write("|                                                                                 |\n")
            file.write(f"|Total Amount: {total_amount:<67}|\n")
            file.write("+---------------------------------------------------------------------------------+\n")

        print("Invoice created: " + invoice_name)
    else:
        print("No lands rented.")

def return_land(lands):
    name = validations.validate_name("Enter your name: ")
    if name is None:
        return

    returned_lands = []
    total_fine = 0

    while True:
        land_id = validations.choose_land_id(lands, available=False)
        if land_id == 0:
            break

        land = next((land for land in lands if land["id"] == land_id and not land["available"]), None)
        if land:
            late_duration = validations.validate_late_duration("Enter late duration (months): ")
            if late_duration == -1:
                continue
            fine = land["price"] * late_duration * 0.1
            total_fine += fine
            returned_lands.append({"id": land_id, "late_duration": late_duration, "fine": fine, "city": land["city"], "direction": land["direction"], "anna": land["anna"], "price": land["price"]})
            land["available"] = True
        else:
            print("Land is available or invalid.")

    if returned_lands:
        write.update_lands_in_file("land_data.txt", lands)  # Update the file after returning
        timestamp = write.generate_timestamp()
        # Get the current date and time
        now = datetime.datetime.now()

        # Format the date and time
        formatted_date_time = now.strftime("%Y/%m/%d %H:%M:%S")

        invoice_name = f"{name}_return_invoice_{timestamp}.txt"  # Add timestamp to invoice name
        with open(invoice_name, "w") as file:
            file.write("+--------------------------------------------------------------------------------------+\n")
            file.write("|                                 TechnoPropertyNepal                                  |\n")
            file.write("+--------------------------------------------------------------------------------------+\n")
            file.write("|                                                                                      |\n")
            file.write(f"|Return Invoice for {name:<67}|\n")  # Adjusted spacing for name
            file.write(f"|Date: {formatted_date_time:<80}|\n")  # Adjusted spacing for date
            file.write("|                                                                                      |\n")
            file.write("+------+--------------+---------------------+------+--------+---------------+----------+\n")
            file.write("|  SN  |     ID       |        City         | Anna | Price  | Late Duration |   Fine   |\n")
            file.write("+------+--------------+---------------------+------+--------+---------------+----------+\n")
            sn = 1
            for returned_land in returned_lands:
                file.write("| {:<4} | {:<12} | {:<19} | {:<4} | {:<6} | {:<13} | {:<8} |\n".format(sn, returned_land['id'], returned_land['city'], returned_land['anna'], returned_land['price'], returned_land['late_duration'], returned_land['fine']))
                sn += 1
            file.write("+------+--------------+---------------------+------+--------+---------------+----------+\n")
            file.write("|                                                                                      |\n")
            file.write(f"|Total Fine: {total_fine:<74}|\n")  # Adjusted spacing for total fine
            file.write("+--------------------------------------------------------------------------------------+\n")


        print("Invoice created: " + invoice_name)
    else:
        print("No lands returned.")