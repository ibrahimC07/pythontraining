from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.page_source)