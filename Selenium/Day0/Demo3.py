from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/v1/")
time.sleep(2)
print("trying to capture the title of the page")
title = driver.title
print(title)
print("trying to capture the current url of this page")
url = driver.current_url
print(url)
pagesource = driver.page_source
print(pagesource)
driver.quit()