from selenium import webdriver
import time
driver=webdriver.Chrome()
time.sleep(5)
driver.get("https://www.google.com/")
time.sleep(5)
driver.get("https://www.saucedemo.com/v1/")
time.sleep(3)
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(3)
#driver.quit()
driver.back()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.back()
time.sleep(2)
driver.refresh()
time.sleep(3)