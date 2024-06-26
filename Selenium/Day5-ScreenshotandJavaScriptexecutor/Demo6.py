import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("file:///D:/Development/repo/pythonRepo1/Selenium/BasicHtmlElement.html")
time.sleep(2)
ele = driver.find_element(By.XPATH, "//input[@value='testing']")
driver.execute_script("arguments[0].click()", ele)
time.sleep(2)
driver.quit()