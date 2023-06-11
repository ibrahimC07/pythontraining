import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.maximize_window()
searchbox = driver.find_element(By.NAME, 'q')
searchbox.send_keys("Selenium")
searchbox.submit()
driver.find_element(By.XPATH, " //h3[text()='Selenium']").click()
