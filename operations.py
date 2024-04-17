import validations
import read
import write

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
    for land in lands:
        print(f"{land['id']}, {land['city']}, {land['direction']}, {land['anna']}, {land['price']}, {'Available' if land['available'] else 'Not Available'}")

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
            rented_lands.append({"id": land_id, "duration": duration, "amount": amount})
            land["available"] = False
        else:
            print("Land is not available.")

    if rented_lands:
        write.update_lands_in_file("land_data.txt", lands)  # Update the file after renting
        timestamp = write.generate_timestamp()
        invoice_name = f"{name}_rent_invoice_{timestamp}.txt"  # Add timestamp to invoice name
        with open(invoice_name, "w") as file:
            file.write(f"Rent Invoice for {name}\n\n")
            file.write("Land ID\tDuration\tAmount\n")
            for rented_land in rented_lands:
                file.write(f"{rented_land['id']}\t{rented_land['duration']}\t{rented_land['amount']}\n")
            file.write(f"\nTotal Amount: {total_amount}\n")

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
            late_duration = validations.validate_duration("Enter late duration (months): ")
            if late_duration == -1:
                continue
            fine = land["price"] * late_duration * 0.1
            total_fine += fine
            returned_lands.append({"id": land_id, "late_duration": late_duration, "fine": fine})
            land["available"] = True
        else:
            print("Land is available or invalid.")

    if returned_lands:
        write.update_lands_in_file("land_data.txt", lands)  # Update the file after returning
        timestamp = write.generate_timestamp()
        invoice_name = f"{name}_return_invoice_{timestamp}.txt"  # Add timestamp to invoice name
        with open(invoice_name, "w") as file:
            file.write(f"Return Invoice for {name}\n\n")
            file.write("Land ID\tLate Duration\tFine\n")
            for returned_land in returned_lands:
                file.write(f"{returned_land['id']}\t{returned_land['late_duration']}\t{returned_land['fine']}\n")
            file.write(f"\nTotal Fine: {total_fine}\n")

        print("Invoice created: " + invoice_name)
    else:
        print("No lands returned.")
