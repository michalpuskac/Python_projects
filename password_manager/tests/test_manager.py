import sys
import os
# Insert the absolute path to the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from manager import add_entry, view_entries, DATA_FILE, set_fernet_instance
from crypto_utils import initialize_fernet


# Fixture to use a temporary file for password storage.
@pytest.fixture
def temp_data_file(tmp_path, monkeypatch):
    temp_file = tmp_path / "passwords.txt"
    monkeypatch.setattr("manager.DATA_FILE", str(temp_file))
    # Start with an empty file.
    temp_file.write_text("")
    return temp_file

# Fixture to create a Fernet instance using a test master password.
@pytest.fixture
def test_fernet():
    return initialize_fernet("testpassword")

def test_add_and_view_entries(monkeypatch, temp_data_file, test_fernet, capsys):
    # Set the global Fernet instance for manager.
    set_fernet_instance(test_fernet)
    
    # Prepare inputs for adding an entry.
    inputs = iter(["TestAccount"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))
    # Since getpass was imported directly in manager, override it there.
    monkeypatch.setattr("manager.getpass", lambda prompt="": "TestPassword")
    
    # Add a new entry.
    add_entry()
    
    # Now, view entries and capture the output.
    view_entries()
    captured = capsys.readouterr().out
    
    assert "TestAccount" in captured
    assert "TestPassword" in captured

def test_view_no_entries(monkeypatch, temp_data_file, test_fernet, capsys):
    set_fernet_instance(test_fernet)
    # Ensure the temporary data file is empty.
    temp_data_file.write_text("")
    view_entries()
    captured = capsys.readouterr().out
    assert "No passwords stored yet." in captured