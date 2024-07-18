from selenium import webdriver
from pages.base_page import BasePage
from pages.contacts_list_page import ContactsListPage
from selenium.webdriver.common.by import By
from apis.user_operations.model import User

class SignUpPage(BasePage):
    
    ADD_USER_LABEL = (By.XPATH, '//h1[text()=\'Add User\']')
    FIRST_NAME_INPUT = (By.ID, 'firstName')
    LAST_NAME_INPUT = (By.ID, 'lastName')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    SUBMIT_BUTTON = (By.ID, 'submit')
    CANCEL_BUTTON = (By.ID, 'cancel')
    
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self._wait.wait_until_element_is_visible(self.ADD_USER_LABEL, 10)
        
    def create_user(self, user_data: User) -> ContactsListPage:
        self.send_keys(self.FIRST_NAME_INPUT, user_data.firstName)
        self.send_keys(self.LAST_NAME_INPUT, user_data.lastName)
        self.send_keys(self.EMAIL_INPUT, user_data.email)
        self.send_keys(self.PASSWORD_INPUT, user_data.password)
        self.click(self.SUBMIT_BUTTON)
        return ContactsListPage(self._driver)
        
        
        
    
    
    