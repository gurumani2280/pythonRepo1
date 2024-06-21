from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///fileLocation/BasicHtmlElement.html")
time.sleep(3)
allgenders = driver.find_elements(By.NAME,'gender')
print(type(allgenders))
for gender in allgenders:
    print(gender.get_attribute('value'))
    print(gender.get_attribute('type'))
    gender.click()

time.sleep(3)

driver.quit()




