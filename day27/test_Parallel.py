import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    def test_login_chrome(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

    def test_login_edge(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

    def test_login_safari(self):
        self.driver = webdriver.Safari()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()
