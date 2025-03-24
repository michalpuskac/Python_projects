import os
from colorama import Fore
from getpass import getpass

# Global constant for the data file.
DATA_FILE = "passwords.txt"

# Global variable to store the Fernet instance.
fer = None

def set_fernet_instance(fernet_instance):
    """
    Sets the global Fernet instance.
    """
    global fer
    fer = fernet_instance

def add_entry():
    """
    Prompts the user for an account and its password, encrypts it,
    and appends it to the passwords file.
    """
    if fer is None:
        print(Fore.RED + "Encryption engine not initialized.")
        return

    account = input(Fore.CYAN + "Account Name: ").strip()
    if not account:
        print(Fore.RED + "Account name cannot be empty.")
        return

    pwd = getpass(Fore.CYAN + "Password: ").strip()
    if not pwd:
        print(Fore.RED + "Password cannot be empty.")
        return

    try:
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()
        with open(DATA_FILE, 'a') as f:
            f.write(f"{account}|{encrypted_pwd}\n")
        print(Fore.GREEN + "Password added successfully.")
    except Exception as e:
        print(Fore.RED + f"Failed to add password: {e}")

def view_entries():
    """
    Reads the passwords file and decrypts each stored password.
    """
    if fer is None:
        print(Fore.RED + "Encryption engine not initialized.")
        return

    if not os.path.exists(DATA_FILE):
        print(Fore.YELLOW + "No passwords stored yet.")
        return

    try:
        with open(DATA_FILE, 'r') as f:
            lines = f.readlines()
            if not lines:
                print(Fore.YELLOW + "No passwords stored yet.")
                return
            for line in lines:
                data = line.rstrip()
                if data:
                    try:
                        account, encrypted_pwd = data.split("|")
                        decrypted_pwd = fer.decrypt(encrypted_pwd.encode()).decode()
                        print(Fore.YELLOW + f"Account: {account} | Password: {decrypted_pwd}")
                    except Exception as e:
                        print(Fore.RED + f"Error decrypting entry for '{account}': {e}")
    except Exception as e:
        print(Fore.RED + f"Failed to read passwords file: {e}")