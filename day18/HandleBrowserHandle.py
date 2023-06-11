import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
# windowid = driver.current_window_handle
# print(windowid)  # IDwindow-24CFB4FFB7CB60C7309293A9217B9F2A I
# driver.close()

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
windowsIDs = driver.window_handles
# parentwindowid = windowsIDs[0]
# childwindowid = windowsIDs[1]
# print(parentwindowid, childwindowid)
#
# driver.switch_to.window(childwindowid)
# print(driver.title)
# driver.switch_to.window(parentwindowid)
# print(driver.title)

# approach : 2
# for winid in windowsIDs:
#     driver.switch_to.window(winid)
#     print(driver.title)

# is there is 10 tab , how we close the tab that we want.
for winid in windowsIDs:
    driver.switch_to.window(winid)
    if driver.title == "OrangeHRM" or driver.title == "OrangeHRM HR Software | Free HR Software | HRMS | HRIS":
        driver.close()
