import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
# Login
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
# Admin-->user management-->users
driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b").click()
driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']").click()
driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']").click()
rows = len(driver.find_elements(By.XPATH, "//table[@id='resultTable']//tbody/tr"))
print("total number of rows in a table:", rows)
count = 0
for r in range(1, rows + 1):
    status = driver.find_element(By.XPATH, "//table[@id='resultTable']/tbody/tr[" + str(r) + "]/td[5]").text
    if status == "Enabled":
        count = count + 1
print("Total Number of users:", rows)
print("Number of enabled users:", count)
print("Number of disabled users:", (rows - count))
