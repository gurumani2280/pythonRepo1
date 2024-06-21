#Check all the checkboxes by using XPATH

from selenium import webdriver

import time
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("file:///fileLocation/BasicHtmlElement.html")
time.sleep(2)
skill_checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(type(skill_checkboxes)) #<class 'list'>
time.sleep(3)
for checkbox in skill_checkboxes:
    checkbox.click()
time.sleep(3)
for checkbox in skill_checkboxes:
    checkbox.click()
time.sleep(3)
driver.quit()