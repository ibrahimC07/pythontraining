import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH, "//button [normalize-space ()='Click for JS Prompt']").click()
time.sleep(2)
alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("welcome")
# alertwindow.accept()  # close alert window by using OK button
alertwindow.dismiss()  # close alert window by using cancel button
time.sleep(2)
