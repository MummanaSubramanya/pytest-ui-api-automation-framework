import pytest

from apis.app import Application
from apis.user_operations.model import RegisterUserResponse, User, ErrorResponse
from utils.random_utils import get_password
from utils.entity_creator import create_new_user_data
from utils.serialize_response import structure_response


@pytest.mark.api
def test_new_user_creation_with_valid_data(app: Application):
    # Generate random user data
    user_data = create_new_user_data()
    
    # Perform create user operation
    new_user = app.user_operations.create_new_user_successfully(user_data)
    assert new_user.user.email.lower() == user_data.email.lower()
    assert new_user.user.firstName.lower() == user_data.firstName.lower()
    assert new_user.user.lastName.lower() == user_data.lastName.lower()
    assert not new_user.user._id == None
    assert not new_user.token == None
    
@pytest.mark.api
def test_new_user_creation_with_existing_data(app: Application, create_user: RegisterUserResponse):
    # Generate random user data
    user = User(firstName = create_user.user.firstName,
                    lastName = create_user.user.lastName,
                    email = create_user.user.email, 
                    password = get_password())
    
    # Perform create user operation with existing details 
    response = app.user_operations.create_new_user_response(user)
    assert response.status_code == 400, "Check status code"
    error_data = structure_response(response, ErrorResponse)
    assert error_data.message == 'Email address is already in use'


@pytest.mark.api
def test_delete_user(app: Application, create_user: RegisterUserResponse):
    # Delete the created user
    app.user_operations.delete_user_successfully(create_user.token)
    
    # Get the deleted user and validate user cannot be accessed
    response = app.user_operations.get_user_response(create_user.token)
    assert response.status_code == 401
    

@pytest.mark.api
def test_get_user(app: Application, create_user: RegisterUserResponse):
    # Get the created user and validate the details
    user_data = app.user_operations.get_user_successfully(create_user.token)
    assert create_user.user.email == user_data.email
    assert create_user.user.firstName == user_data.firstName
    assert create_user.user.lastName == user_data.lastName
    assert not user_data._id == None
    
    