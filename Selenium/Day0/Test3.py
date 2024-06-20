from selenium import webdriver
import time
driver = webdriver.Edge()
time.sleep(5)
driver.get("https://www.selenium.dev/downloads/")
time.sleep(5)
driver.quit()