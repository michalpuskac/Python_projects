import sys
import os

# Insert the absolute path to the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from crypto_utils import get_salt, derive_key, SALT_FILE

def test_get_salt(tmp_path, monkeypatch):
    # Redirect SALT_FILE to a temporary file.
    temp_salt = tmp_path / "salt.salt"
    monkeypatch.setattr("crypto_utils.SALT_FILE", str(temp_salt))
    
    # Ensure the file doesn't exist, then create and read it.
    if temp_salt.exists():
        temp_salt.unlink()
    salt = get_salt()
    assert salt is not None
    assert len(salt) == 16
    
    # Calling again should retrieve the same salt.
    salt2 = get_salt()
    assert salt == salt2

def test_derive_key():
    master_password = "testpassword"
    salt = b"1234567890123456"  # 16 bytes salt
    key1 = derive_key(master_password, salt)
    key2 = derive_key(master_password, salt)
    # The keys must match for the same password and salt.
    assert key1 == key2
    # Fernet keys are base64-encoded 32-byte keys (should be 44 characters).
    assert isinstance(key1, bytes)
    assert len(key1) == 44