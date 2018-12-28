from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from demo.locators.globalLocators import globalLocators

class HomePage():

    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 30)
        self.driver.set_page_load_timeout(30)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.user_login_text = globalLocators.user_login_text

    def verifyUserLoggedIn(self):
        elementLoginID = self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.user_login_text)))
        print(elementLoginID.text)