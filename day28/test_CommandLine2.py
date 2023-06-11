import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestCLI:
    def test_Logo(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()  # Signin
        time.sleep(3)
        try:
            self.status = self.driver.find_element(By.XPATH, "//img[@alt='client brand banner']").is_displayed()
            self.driver.close()
            assert self.status == True
        except:
            self.driver.close()
            assert False

    def test_Login(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()  # Signin
        time.sleep(3)
        try:
            self.status = self.driver.find_element(By.XPATH, "//img[@alt='client brand banner']").is_displayed()
            self.driver.close()
            assert self.status == True
        except:
            self.driver.close()
            assert False
