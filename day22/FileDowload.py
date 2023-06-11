import time

from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

location = os.getcwd()


# def chrome_setup():
#     from selenium import webdriver
#     preferences = {"download.default_directory": location}
#     ops = webdriver.ChromeOptions()
#     ops.add_experimental_option("prefs", preferences)
#     driver = webdriver.Chrome(options=ops)
#     return driver


# def edge_setup():
#     from selenium.webdriver.edge.service import Service
#     from selenium import webdriver
#     preferences = {"download.default_directory": location}
#     ops = webdriver.EdgeOptions()
#     ops.add_experimental_option("prefs", preferences)
#     driver = webdriver.Edge(options=ops)
#     return driver
def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C: \Drivers\geckodriver-vo.29.1-win64\geckodriver.exe")
    # settings
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser. helperApps.neverAsk.saveToDisk", "application/msword")
    ops.set_preference("browser. download. manager. showWhenStarting", False)
    ops.set_preference("browser. download.folderList", 2)  # 0-desktop 1-downloads folder 2- Desired loc
    ops.set_preference("browser. download.dir", location)
    driver = webdriver.Firefox(service=serv_obj, options=ops)
    return driver


# driver = chrome_setup()
# mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
#                                                                          ElementNotVisibleException,
#                                                                          ElementNotSelectableException,
#                                                                          Exception])

# driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
# driver.maximize_window()
# den = mywait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='https://file-examples.com/wp-content"
#                                                                     "/storage/2017/02/file-sample_100kB.doc']")))
#
# den2 = mywait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#page-top")))
# den.click()
# den2.click()
# time.sleep(3)
