from selenium import webdriver
import time
driver=webdriver.Chrome()
time.sleep(3)
driver.get("https://www.dinamalar.com/")
time.sleep(3)
title=driver.title
print(title)
url=driver.current_url
print(url)
#pagesource=driver.page_source
#print(pagesource)