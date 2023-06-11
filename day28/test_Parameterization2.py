import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestClass:
    @pytest.mark.parametrize('user,pwd',
                             [("Admin", "admin123"),
                              ("adm", "admin123"),
                              ("Admin", "adm"),
                              ("adm", "adm")
                              ]
                             )
    def test_Login(self, user, pwd):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(user)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(pwd)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()  # Signin
        try:
            self.status = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Dashboard']").is_displayed()
            self.driver.close()
            assert self.status == True
        except:
            self.driver.close()
            assert False
