from pages.signIn_page import SignInPage
from utils.entity_creator import create_new_user_data
import pytest

@pytest.mark.web
def test_create_user_with_valid_data(create_driver):
    # Pre-requisite to create user
    user = create_new_user_data()
    
    # Create user in application
    sign_page = SignInPage(create_driver)
    contacts_list_page = (sign_page
     .navigate_to_signup_page()
     .create_user(user))
    
    assert contacts_list_page.get_contact_table().is_displayed() == True
    
    