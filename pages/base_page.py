from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from utils.waits import Wait

class BasePage:
    
    def __init__(self, driver: webdriver) -> None:
        self._driver = driver
        self._wait = Wait(driver)
    
    def find_element(self, locator: object):
        return self._wait.wait_until_element_is_present(locator, 10)
    
    def click(self, locator: object):
        self.find_element(locator).click()

    def send_keys(self, locator: object, text: str):
        self.find_element(locator).send_keys(text)
        
    