from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://thinking-tester-contact-list.herokuapp.com')
driver.maximize_window()
time.sleep(4)
locator1 = (By.ID, "email")
locator2 = (By.ID, "password")
wait = WebDriverWait(driver, timeout=10)
wait.until(EC.element_to_be_clickable(locator1))
wait.until(EC.visibility_of_element_located(locator1))
driver.find_element(By.ID, "email").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("adminpassword")
driver.find_element(By.ID, "password").is_displayed()
time.sleep(5)

