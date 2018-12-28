from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from demo.locators.globalLocators import globalLocators
class LoginPage():

    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 30)
        self.driver.set_page_load_timeout(30)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.username_textbox_ID = globalLocators.username_textbox_ID
        self.password_textbox_ID = globalLocators.password_textbox_ID
        self.login_button = globalLocators.login_button

    def enterUserName(self,username):
        elementUserName = self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,self.username_textbox_ID)))
        elementUserName.send_keys(username)

    def enterPassword(self,password):
        elementPassword = self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH,self.password_textbox_ID)))
        elementPassword.send_keys(password)

    def clickLogin(self):
        elementLogin = self.wait.until(
        expected_conditions.element_to_be_clickable((By.XPATH,self.login_button)))
        elementLogin.click()
