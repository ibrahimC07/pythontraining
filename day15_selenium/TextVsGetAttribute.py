import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

emailbox = driver.find_element(By.XPATH, "//input[@id='Email']")
emailbox.clear()
emailbox.send_keys("abc@gmail.com")
time.sleep(2)

print("result of text:", emailbox.text)
print("result of get_attribute ():", emailbox.get_attribute ('value'))

driver.quit()