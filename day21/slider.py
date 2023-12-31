import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider = driver.find_element(By.XPATH, "//body//div//span[1]")
max_slider = driver.find_element(By.XPATH, "//body//div//span[2]")
print("Location of sliders Before moving........")
print(min_slider.location)  # {'x': 59,'y': 252}
print(max_slider.location)  # {'x': 639, '4': 252}
act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider, 100, 0).perform()
act.drag_and_drop_by_offset(max_slider, -39, 0).perform()
time.sleep(3)

print("Location of sliders After moving........")
print (min_slider. location) # {'x': 158, 'y': 252}
print (max_slider.location) # {'x': 598, 'y': 252}
