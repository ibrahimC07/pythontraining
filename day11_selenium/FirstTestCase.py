# Test Case
# ----------
# 1) Open Web Browser(Chrome/firefox/Edge).
# 2) Open URL https://opensource-demo.orangehrmlive.com/
# 3) Enter username(Admin).
# 4) Enter password (admin123).
# 5) Click on Login.
# 6) Capture title of the home page. (Actual title)
# 7) Verify title of the page: OrangeHRM(Expected)
# 8) close browser

from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome(executable_path="/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys("Admin")
# driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("admin123")
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# serv_obj = Service("/Users/ibrahimcelikel/Downloads/chromedriver_mac_arm64")
driver = webdriver.Chrome()
# driver = webdriver.Chrome(service=serv_obj)
driver.get("https://google.com/")
# wait = WebDriverWait(driver, 10)
element = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
element.send_keys("Admin")
element.send_keys(Keys.ENTER)
element3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "a[href='/search?q=Admin&sxsrf=APwXEdfgP9ODJmCFdd1RQzSawuexekHwjg:1685826343935&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiKgYjDgKj_AhWKcPEDHS8sAfwQ_AUoAXoECAEQAw']"))) 
#element2 = driver.find_element(By.XPATH, "a[href='/search?q=Admin&sxsrf=APwXEdfgP9ODJmCFdd1RQzSawuexekHwjg:1685826343935&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiKgYjDgKj_AhWKcPEDHS8sAfwQ_AUoAXoECAEQAw']")
# driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("admin123")
# driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
