import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# regilint = Keys.COMMAND + Keys.RETURN
# driver.find_element(By.LINK_TEXT, "Register").send_keys(Keys.COMMAND + Keys.RETURN)
# time.sleep(3)
driver.switch_to.new_window('tab')
driver.get("https://opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://orangehrm.com/")
