from selenium import webdriver
import time
driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://www.selenium.dev/downloads/")
time.sleep(5)
driver.quit()