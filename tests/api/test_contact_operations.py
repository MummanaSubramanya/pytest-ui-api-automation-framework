import pytest
from apis.app import Application
from apis.user_operations.model import RegisterUserResponse, User
from utils.entity_creator import create_new_contact_data

@pytest.mark.api
def test_new_contact_creation_with_valid_data(app: Application, create_user: RegisterUserResponse):
    # Generate random contact data to add
    contact_data = create_new_contact_data()
    
    # Perform create user operation
    new_contact = app.contact_operations.create_new_contact_successfully(create_user.token, contact_data)
    assert contact_data.firstName == new_contact.firstName
    assert contact_data.email.lower() == new_contact.email.lower()
    assert not None == new_contact.owner