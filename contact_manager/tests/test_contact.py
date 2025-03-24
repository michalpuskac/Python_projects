import sys
import os

# Insert the absolute path to the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
import json
from contacts import ContactManager 

@pytest.fixture
def manager(tmp_path):
    """Fixture to create a ContactManager with a temporary test file."""
    file_path = tmp_path / "test_contacts.json"
    return ContactManager(file_path=str(file_path))

def test_add_new_contact(manager):
    """Test adding a new contact."""
    manager.add_new_contact("Bob Marley", "+1234567890")
    assert "bob marley" in manager.contacts
    assert manager.contacts["bob marley"] == "+1234567890"

def test_search_contact_found(manager):
    """Test searching for an existing contact."""
    manager.add_new_contact("Fred Flinstone", "+0987654321")
    result = manager.search_contact("Fred Flinstone")
    assert "+0987654321" in result

def test_search_contact_not_found(manager):
    """Test searching for a non-existing contact."""
    result = manager.search_contact("Nonexistent")
    assert result == "Contact not Found\n"

def test_delete_contact(manager):
    """Test deleting a contact."""
    manager.add_new_contact("Delete Me", "+1111111111")
    manager.delete_contact("Delete Me")
    assert "delete me" not in manager.contacts

def test_save_and_load_contacts(manager):
    """Test saving and loading contacts."""
    manager.add_new_contact("Save Test", "+2222222222")
    manager._save_contacts()
    # Create a new manager instance to simulate reloading
    new_manager = ContactManager(manager.file_path)
    assert "save test" in new_manager.contacts
    assert new_manager.contacts["save test"] == "+2222222222"`