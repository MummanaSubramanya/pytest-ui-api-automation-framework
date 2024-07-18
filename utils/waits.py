from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Wait:
    
    def __init__(self, driver) -> None:
        self._driver = driver

 
    def wait_until_element_is_present(self, webelement, timeout):
        wait = WebDriverWait(self._driver, timeout=timeout)
        return wait.until(expected_conditions.presence_of_element_located(webelement))


    def wait_until_element_is_visible(self, webelement, timeout):
        wait = WebDriverWait(self._driver, timeout=timeout)
        return wait.until(expected_conditions.visibility_of_element_located(webelement))
    
        