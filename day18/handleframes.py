import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
# driver.maximize_window()
# driver.switch_to.frame("packageListFrame")
# driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
# driver.switch_to.default_content()  # go back to main page
# driver.switch_to.frame("packageFrame")
# driver.find_element(By.LINK_TEXT, "WebDriver").click()
# driver.switch_to.default_content()  # No back to main page
# driver.switch_to.frame("classFrame")
# driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()

# inner frames
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()
outerframe = driver.find_element(By.XPATH, "//iframe [@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)
innerframe = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("welcome")
time.sleep(2)
