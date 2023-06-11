import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

mywait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                         ElementNotVisibleException,
                                                                         ElementNotSelectableException,
                                                                         Exception]
                       )
searchlink = mywait.until(EC.invisibility_of_element((By.XPATH, "//a[@class='btn btn-link navbar-btn']")))
drpcountry = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))
# select option fro th dropdown
drpcountry.select_by_visible_text("India")
time.sleep(3)

# capture all the options and print them
alloptions = drpcountry.options
print("total number of options:", len(alloptions))
# for opt in alloptions:
#     print(opt.text)

# select option from dropdown without using built-in method
# for opt in alloptions:
#     if opt.text == "India":
#         opt.click()
#     break
# if there is no select class use this
allOptions = driver.find_elements(By.XPATH, '//*[@id="input-country"]/option')
print(len(allOptions))
for opt in alloptions:
    print(opt.text)
for opt in alloptions:
    if opt.text == "India":
        opt.click()
    break
