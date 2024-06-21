from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/v1/")
time.sleep(5)
username=driver.find_element(By.ID,"user-name")
print("the username is identified successfully")
username.send_keys("standard_use")
time.sleep(3)
password=driver.find_element(By.ID,"password")
print("the password is identified successfully")
password.send_keys("secret_sauce")
time.sleep(5)
driver.find_element(By.ID,"login-button").click()
time.sleep(5)
print(driver.title)
print(driver.current_url)