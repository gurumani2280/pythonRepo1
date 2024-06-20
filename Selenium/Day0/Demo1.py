from selenium import webdriver
import time
print("launching chrome browser")
driver = webdriver.Chrome()
time.sleep(5)
print("maximising the chrome browser")
driver.maximize_window()
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
print("closing chrome browser")
driver.quit()