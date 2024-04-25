import operations
import read
import validations

def start():
    lands = read.load_lands_from_file("land_data.txt")
        
    while True:
        operations.welcome_screen()
        choice = validations.choose_option()
        if choice == 1:
            operations.display_lands(lands)
            operations.rent_land(lands)
        elif choice == 2:
            operations.display_lands(lands)
            operations.return_land(lands)
        elif choice == 3:
            print("Exiting TechnoPropertyNepal...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    start()
