from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/v1/")
time.sleep(2)
driver.get("https://www.google.com/")
time.sleep(2)
driver.get("https://www.selenium.dev/downloads/")
print("navigating backward using back method")
driver.back()
time.sleep(5)
driver.back()
time.sleep(3)
print("navigating forward using forward method")
driver.forward()
print("reloading the page")
time.sleep(3)
driver.refresh()
time.sleep(5)
driver.quit()