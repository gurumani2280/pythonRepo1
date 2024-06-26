import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///D:/Development/repo/pythonRepo1/Selenium/BasicHtmlElement.html")
time.sleep(2)
driver.execute_script("document.getElementById('firstname').value='admin'")
time.sleep(2)
driver.close()