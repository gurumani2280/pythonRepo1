from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///fileLocation/BasicHtmlElement.html")
time.sleep(3)
allcheckboxes = driver.find_elements(By.NAME,'skill')
print(type(allcheckboxes))
print(len(allcheckboxes))
for checkbox in allcheckboxes:
    print(checkbox.get_attribute('value'))
    print(checkbox.get_attribute('type'))
    checkbox.click()


time.sleep(3)
for checkbox in allcheckboxes:
    checkbox.click()                  #unchecking the checkboxes

time.sleep(3)

driver.quit()




