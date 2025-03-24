from contacts import ContactManager
from pyfiglet import figlet_format
from colorama import Fore, Style, init

# Initialize Colorama (in case it isn't already)
init(autoreset=True)

def menu():
    print("\n" + Fore.CYAN + "---Contact Manager Menu---")
    print(Fore.CYAN + "1. Add new contact")
    print(Fore.CYAN + "2. Show all contacts")
    print(Fore.CYAN + "3. Search contact")
    print(Fore.CYAN + "4. Delete contact")
    print(Fore.CYAN + "5. Export all contacts to CSV")
    print(Fore.CYAN + "Type 'exit' to quit the program\n")

def main():
    # Display a stylish banner using pyfiglet
    banner = figlet_format("Contact Manager", font="slant")
    print(Fore.MAGENTA + banner)
    
    manager = ContactManager()
    menu()
    
    while True:
        choice = input(Fore.WHITE + "What do you want to do? Choose 1, 2, 3, 4, or 5: ").strip().lower()
        if choice not in {"1", "2", "3", "4", "5", "exit"}:
            print(Fore.RED + "Invalid input. Try again with choice 1 to 5 or 'exit'\n")
            continue
        
        if choice == "1":
            name = input("Enter name of contact: ").strip()
            number = input(f"Enter number for contact {name}: ").strip()
            manager.add_new_contact(name, number)

        elif choice == "2":
            manager.show_all_contacts()
            menu()

        elif choice == "3":
            name = input("Enter name of the contact you want to find: ").strip()
            print(manager.search_contact(name))

        elif choice == "4":
            name = input("Enter name of the contact you want to delete: ").strip()
            manager.delete_contact(name)

        elif choice == "5":
            manager.export_to_csv()

        elif choice == "exit":
            print(Fore.GREEN + "Program terminated.")
            break

if __name__ == "__main__":
    main()