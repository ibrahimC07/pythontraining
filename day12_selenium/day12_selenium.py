from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://google.com")
driver.maximize_window()  # maximize the browser window
sliders = driver.find_elements(By.XPATH, "//head")
print(len(sliders))
links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))
