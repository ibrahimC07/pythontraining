import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
# 1. Scroll down page by pixel
# driver.execute_script("window.scrollBy(0,3000)", "")
# time.sleep(3)
# value = driver.execute_script("return window.pageYOffset;")
# time.sleep(3)
#
# print("number of pixels moved :", value)  # 3000

# 2. Scroll down page till the element is visible
# flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved:", value)  # 5038.3330078125
# time.sleep(3)

# 3.scroll down page till end
driver.execute_script("window.scrollBy(0, document .body .scrollHeight)")
value = driver.execute_script("return window.pageOffset;")
time.sleep(3)
print("Number of pixels moved:", value)
# Scroll up to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(3)
