import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
# Date of birth
driver.find_element(By.XPATH, "//input[@id='dob']").click()  # opens date picker
datepicker_month = Select(driver.find_element(By.XPATH, "//select[@data-handler='selectMonth']"))
datepicker_month.select_by_visible_text("Dec")  # month
datepicker_year = Select(driver.find_element(By.XPATH, "//select[@data-handler='selectYear']"))
datepicker_year.select_by_visible_text("1999")
alldates = driver.find_elements(By.XPATH, "//div[@id='vi-datepicker-div']//table/tbody/tr/td/a")
for date in alldates:
    if date.text == "25":
        date.click()
        break
time.sleep(3)
