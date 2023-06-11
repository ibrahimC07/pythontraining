from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    ops = webdriver.ChromeOptions()
    ops.headless= True
    driver = webdriver.Chrome(options=ops)
    return driver


driver = headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()