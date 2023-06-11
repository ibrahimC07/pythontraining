# we need to install requests package through file --> ....
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://google.com/")
driver.maximize_window()

allLinks = driver.find_elements(By.TAG_NAME, 'a')
count = 0
for link in allLinks:
    url = link.get_attribute('href')
    try:
     res = requests.head(url)
    except:
        None
    if res.status_code >= 400:
        print(url, " is broken link")
        count += 1
    else:
        print(url, "   is valid link")
print("total number of broken links:", count)
