import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

# 2) Locator matching with multiple webelements
element = driver.find_element(By.XPATH, "//div[@class='footer']//a")
print(element.text)  # prints first link from the footer "Sitemap

# 1)Locator matching with single webelement
elements = driver.find_elements(By.XPATH, "//input [@id='small-searchterms']")
print(len(elements))  # 1
elements[0].send_keys("apple")
time.sleep(2)
print(elements[0].get_attribute("value"))

# 2) Locator matching with multiple webelements
elements = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(len(elements))  # 23
print(elements[0].text)
for ele in elements:
    print(ele.text)
