from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import HtmlTestRunner
import unittest
import sys
import os
#sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from demo.Pages.HomePage_test import HomePage
from demo.Pages.LoginPage_test import LoginPage

class HRMProject(unittest.TestCase):

    def setUp(self):
        print("Test Started")
        self.driver = webdriver.Chrome("C:/Users/Sanket/Downloads/chromedriver_win32/chromedriver.exe")

    def test_loginHRM(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        loginPage = LoginPage(driver)
        loginPage.enterUserName("Admin")
        loginPage.enterPassword("admin123")
        loginPage.clickLogin()

        homePage = HomePage(driver)
        homePage.verifyUserLoggedIn()

        # try:
        #     elementUserName = self.wait.until(
        #     expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='txtUsername']")))
        #     elementUserName.send_keys("Admin")
        #
        #     elementPassword = self.wait.until(
        #         expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='txtPassword']")))
        #     elementPassword.send_keys("admin123")
        #
        #     elementLogin = self.wait.until(
        #         expected_conditions.element_to_be_clickable((By.XPATH, "//input[@id='btnLogin']")))
        #     elementLogin.click()
        #
        #     elementLoginID = self.wait.until(
        #         expected_conditions.visibility_of_element_located((By.XPATH, "//a[@id='welcome']")))
        #     print(elementLoginID.text)
        #
        # except:
        #     print("Element is not visible")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Finish")

if __name__== '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="F:/Study Document/Python Selenium/ResultHTML"))