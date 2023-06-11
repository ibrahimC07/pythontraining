import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# 1) select specific checkbox
# driver.find_element (By.XPATH, "//input[@id='monday']").click)
# 2) select all the checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
print(len(checkboxes))  # 7

# Approach1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()
# time.sleep(3)

# Approach2
# for checkbox in checkboxes:
#      checkbox.click()
# time.sleep(3)

# time.sleep(3)

# approach 3 : select multiple checkboxes by choice
# for checkbox in checkboxes:
#     weekname = checkbox.get_attribute("id")
#     if weekname == "monday" or weekname == "sunday":
#         checkbox.click()
# time.sleep(3)
# 4 ) select last 2 checkboxes
# range (5, 7) -->6, 7
# for i in range(len(checkboxes) - 2, len(checkboxes)):
#     checkboxes[i].click()
# time.sleep(3)
# 5) select first 2 checkboxes
# for i in range(len(checkboxes)):
#     if i < 2:
#         checkboxes[i].click()
# time.sleep(3)

# 6) clearing all the check boxes
# for checkbox in checkboxes:
#     if checkbox.is_selected():
#         checkbox.click()
# time.sleep(3)