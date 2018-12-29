from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import pytest
import time
import unittest

class TestSample:
    @pytest.fixture()
    def test_SetUp(self):
        print("Test Started")
        global wait
        global driver
        driver = webdriver.Chrome("C:/Users/Sanket/Downloads/chromedriver_win32/chromedriver.exe")
        wait = WebDriverWait(driver, 30)
        driver.set_page_load_timeout(30)
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        #driver.get("https://www.google.com")
        yield
        driver.close()
        driver.quit()
        print("Test Finish")

    def test_loginHRM(self,test_SetUp):
        elementUserName = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='txtUsername']")))
        elementUserName.send_keys("Admin")

        elementPassword = wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='txtPassword']")))
        elementPassword.send_keys("admin123")

        elementLogin = wait.until(
             expected_conditions.element_to_be_clickable((By.XPATH, "//input[@id='btnLogin']")))
        elementLogin.click()

        elementLoginID = wait.until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//a[@id='welcome']")))
        print(elementLoginID.text)

    # def test_TearDown():
    #     driver.close()
    #     driver.quit()
    #     print("Test Finish")

    # if __name__ == '__main__':
    #     unittest.main(testRunner=HtmlTestRunner.ht)