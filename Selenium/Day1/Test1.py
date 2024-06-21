from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///fileLocation/BasicHtmlElement.html")
time.sleep(3)
#driver.find_element(By.NAME,'gender').click()     #This will click on the first avaialble element when multile value is there with teh same name
driver.find_element(By.XPATH,'//input[@value="f"]').click()
#driver.find_element(By.XPATH,'//input[@value="testing1"]').click()      #NoSuchElementException
time.sleep(3)

driver.quit()




