from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()
# self
text_msg = driver.find_element(By.XPATH, "//a[normalize-space()='Globus Spirits Ltd.']").text
print(text_msg)  # India Tourism De
