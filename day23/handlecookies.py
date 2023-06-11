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

cookies = driver.get_cookies()
print(len(cookies))

# for c in cookies:
#     #print(c)
#     print(c.get("name"), ":", c.get("value"))

# Add new cookie to the browser
driver.add_cookie({"name": "MyCookie", "value": "123456"})
cookies = driver.get_cookies()
print("Size of cookies after adding new one:", len(cookies))

# Delete specific cookie from the browser
driver.delete_cookie("MyCookie")
cookies = driver.get_cookies()
print("Size of cookies after deleted one:", len(cookies))

# delete all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Size of cookies after deleted all:", len(cookies))
