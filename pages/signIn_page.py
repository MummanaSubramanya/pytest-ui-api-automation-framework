from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.signup_page import SignUpPage
from pages.contacts_list_page import ContactsListPage

# test123_vasu@gmail.com
# password@123

class SignInPage(BasePage):
    
    USERNAME_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_BUTTON = (By.ID, "submit")
    SIGNUP_BUTTON = (By.ID, 'signup')
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def enter_user_name(self, name):
        self.send_keys(self.USERNAME_FIELD, name)
    
    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)
        
    def login_to_application(self, user_name, password):
        self.enter_user_name(user_name)
        self.enter_password(password)
        self.click(self.SIGN_IN_BUTTON)
        return ContactsListPage(self._driver)
    
    def navigate_to_signup_page(self):
        self.click(self.SIGNUP_BUTTON)
        return SignUpPage(self._driver)