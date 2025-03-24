import pyfiglet
from colorama import Fore, init
from manager import add_entry, view_entries

# Initialize colorama for colored terminal output.
init(autoreset=True)

def display_banner():
    """
    Displays a stylized banner using pyfiglet.
    """
    banner = pyfiglet.figlet_format("Pass Manager")
    print(Fore.GREEN + banner)

def menu_loop():
    """
    Runs the main menu loop, allowing users to add or view password entries.
    """
    while True:
        print(Fore.MAGENTA + "\nMenu:")
        print("1. Add a new password")
        print("2. View stored passwords")
        print("q. Quit")
        choice = input(Fore.CYAN + "Enter your choice: ").lower().strip()
        
        if choice == "q":
            print(Fore.MAGENTA + "Exiting Password Manager. Goodbye!")
            break
        elif choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        else:
            print(Fore.RED + "Invalid option. Please select '1', '2', or 'q'.")