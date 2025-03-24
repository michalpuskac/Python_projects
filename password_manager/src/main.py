from ui import display_banner, menu_loop
from crypto_utils import initialize_fernet
from manager import set_fernet_instance
from getpass import getpass
from colorama import Fore

def main():
    display_banner()
    master_password = getpass(Fore.CYAN + "Enter your master password: ")
    fernet_instance = initialize_fernet(master_password)
    set_fernet_instance(fernet_instance)
    menu_loop()

if __name__ == "__main__":
    main()