import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/index.htm")
time.sleep(2)
ele = driver.find_element(By.XPATH, "//h5[text()='About us']")
#How do I scroll based on the visibility of the Web element on the page in Selenium?
driver.execute_script("arguments[0].scrollIntoView();", ele)
time.sleep(2)
driver.quit()