import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
# driver = webdriver.Chrome(service=serv_obj)
ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=ops)
driver.implicitly_wait(10)
driver.get("https://whatmylocation.com/")
driver.maximize_window()
time.sleep(3)