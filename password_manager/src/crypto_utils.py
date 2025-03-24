import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# File to store the salt
SALT_FILE = "salt.salt"

def get_salt():
    """
    Retrieves a salt from a file or creates a new one if it doesn't exist.
    """
    if os.path.exists(SALT_FILE):
        with open(SALT_FILE, "rb") as f:
            salt = f.read()
    else:
        salt = os.urandom(16)  # Generate a new 16-byte salt
        with open(SALT_FILE, "wb") as f:
            f.write(salt)
    return salt

def derive_key(master_password, salt):
    """
    Derives a Fernet-compatible key from the master password using PBKDF2HMAC.
    """
    password_bytes = master_password.encode()  # Convert the password to bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,          # Required length for Fernet key
        salt=salt,
        iterations=100000,  # More iterations increases security
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password_bytes))

def initialize_fernet(master_password):
    """
    Initializes a Fernet instance using a master password.
    """
    salt = get_salt()
    key = derive_key(master_password, salt)
    return Fernet(key)