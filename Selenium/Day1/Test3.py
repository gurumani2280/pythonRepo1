from selenium import webdriver

import time
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("file:///fileLocation/BasicHtmlElement.html")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@value='selenium']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@value='testing']").click()
time.sleep(3)
java_checkbox=driver.find_element(By.XPATH,"//input[@value='java']")
print(type(java_checkbox)) #<class 'selenium.webdriver.remote.webelement.WebElement'>
java_checkbox.click()
time.sleep(3)

driver.quit()