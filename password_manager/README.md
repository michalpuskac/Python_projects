# Password Manager

---

A simple command-line password manager built in Python. This application securely stores and retrieves passwords for various accounts using encryption with a master password. It also features a stylized terminal banner with **pyfiglet** and colored output via **colorama**.

## Features

- **Secure Storage:** Encrypts passwords with a key derived from a master password using PBKDF2HMAC and Fernet.
- **Command-Line Interface:** Easy-to-use menu for adding and viewing password entries.
- **Enhanced Terminal Output:** Uses pyfiglet for a banner and colorama for colorful text.
- **Modular Design:** Code is split into modules for cryptography, password management, and user interface.
- **Testing:** Includes pytest-based tests to ensure core functionality works as expected.


## Directory Structure
```
    password_manager/
    ├── src/
    │   ├── init.py                # Makes the src directory a package.
    │   ├── crypto_utils.py        # Handles salt generation, key derivation, and Fernet initialization.
    │   ├── manager.py             # Provides functions to add and view password entries.
    │   ├── ui.py                  # Manages the user interface, including the menu and banner.
    │   └── main.py                # Main entry point that ties everything together.
    ├── tests/
    |   ├── init.py                # Makes the tests directory a package.
    │   ├── test_crypto_utils.py   # Pytest tests for crypto_utils module.
    │   └── test_manager.py        # Pytest tests for manager module.
    └── requirements.txt           # Project dependencies.
```
## Requirements

- Python 3.8+
- pip (Python package installer) 

    or 
- poetry (Python dependency manager)

## Installation

1. **Clone the repository:**
```bash
    git clone <https://github.com/michalpuskac/Python_projects.git>
    cd password_manager
```

2.	Set up a virtual environment (optional but recommended):
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3.	Install the required dependencies:
```bash
    pip install -r requirements.txt
```

### Using Poetry
1. **Install Poetry:**
```bash
    pip install poetry
```

2. **Install dependencies:**
```bash
    poetry install
```

---

## Usage
1. **Poetry**
```bash
    poetry run python src/main.py
```

2. OR **Virtual enviroment**
```bash
    python src/main.py
```

The application will prompt you for your master password and then display a menu where you can add new passwords or view existing entries.

## Running tests

```bash
    # In virtual enviroment
    pytest tests/

    # In poetry navigate firt to tests folder
    cd tests
    poetry run pytest .
```
This command will discover and run all tests in the tests/ directory.


## Dependencies

 - [cryptography](https://pypi.org/project/cryptography/): For encryption and decryption.
 - [pyfiglet](https://pypi.org/project/pyfiglet/): For generating a stylized ASCII art banner.
 - [colorama](https://pypi.org/project/colorama/): For colorful terminal text.
 - [pytest](https://pypi.org/project/pytest/): For running the test suite.


All dependencies are listed in the requirements.txt or pyproject.toml  file.

## Notes
 - Master Password & Salt: The master password is used to derive an encryption key. A salt is stored in salt.salt to ensure key derivation is consistent across sessions.
 - Data Storage: Encrypted passwords are stored in passwords.txt. Ensure this file is protected appropriately.
 - Security Considerations: This application is for educational purposes. Consider additional security measures if you plan to use it in a production environment, or simply don't use it in production enviroment.

## License
This project is licensed under the MIT License.Feel free to use, modify, and distribute this application as per the terms of the license.

## Author - Michal Puškáč

This project is part of my portfolio, showcasing the basic python skills and concepts. If you have any questions, feedback, or would like to collaborate, feel free to get in touch!

---
- **LinkedIn**:(linkedin.com/in/michal-puškáč-94b925179)
- **GitHub**: (github.com/michalpuskac)

---
