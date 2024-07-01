from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///D:/Development/repo/pythonRepo1/Selenium/Demo2.html")
time.sleep(2)
driver.find_element(By.ID, "t1").send_keys("oldData")
# switch to 1st frame
driver.switch_to.frame(0)
driver.find_element(By.ID, "t2").send_keys("someData")

# back to default web page frame
driver.switch_to.default_content()
driver.find_element(By.ID, "t1").send_keys("newData")

time.sleep(2)
driver.quit()

