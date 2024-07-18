from pages.signIn_page import SignInPage
import pytest

from utils.constants import USER_PASSWORD


@pytest.mark.web
def test_login_with_valid_data(create_driver, create_user):
    # Login to application with the created user
    sign_in = SignInPage(create_driver)
    contacts_list_page = sign_in.login_to_application(create_user.user.email, USER_PASSWORD)
    
    # Validate user is loggedin
    assert contacts_list_page.get_contact_table().is_displayed() == True