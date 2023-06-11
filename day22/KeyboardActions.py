# Ctrl + A
# Ctrl + C
# Tab
# Ctrl + V


import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")
driver.maximize_window()
input1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")
input1.send_keys("welcome to selenium")
input1.click()
act = ActionChains(driver)
# input1 ---> Ctrl+A _Select the text
# act.key_down (Keys.CONTROL)
# act.send_keys("a")
# act.key_up (Keys.CONTROL)
# act.perform()


act.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()
time.sleep(2)

# input1 --->Ctrl+C Copy text
# act. key_down (Keys.CONTROL)
# act.send_keys("c")
# act. key_up (Keys.CONTROL)
# act.performO
act.key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).perform()
# Press Tab key to navigate to input2( second)
# act. send_keys (Keys. TAB)
# act.perform()
act.send_keys(Keys.TAB).perform()
# input2 --›Ctrl+V PasT the text
act.key_down(Keys.COMMAND)
act.send_keys("v")
act.key_up(Keys.COMMAND)
time.sleep(3)
