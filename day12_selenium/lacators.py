from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://facebook.com/")
driver.maximize_window()

# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")
# tag and class
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@gmail.com")

