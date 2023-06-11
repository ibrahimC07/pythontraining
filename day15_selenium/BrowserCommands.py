import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
time.sleep(5)

driver.close()
time.sleep(3)
