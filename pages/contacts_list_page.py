from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ContactsListPage(BasePage):
    
    CONTACT_LIST__LABEL = (By.XPATH, '//h1[text()=\'Contact List\']')
    CONTACT_TABLE = (By.CLASS_NAME,'contactTable')
    
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self._wait.wait_until_element_is_visible(self.CONTACT_LIST__LABEL, 10)
    
    def get_contact_table(self):
        return self.find_element(self.CONTACT_TABLE)