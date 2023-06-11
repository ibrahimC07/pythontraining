from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

# is_displayed() is_enabled()
searchbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Display status:", searchbox.is_displayed())
print("Enabled status:", searchbox.is_enabled())

# is_selected() - for radio buttons and check boxes
rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")
print(rd_male.is_selected())
print(rd_female.is_selected())

rd_male.click()  # select male radio button
print("After selecting male radio button.....")
print(rd_male.is_selected())  # True
print(rd_female.is_selected())  # False
