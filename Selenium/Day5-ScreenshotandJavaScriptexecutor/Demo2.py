import time

from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://pythonbasics.org")
js = 'alert("Hello World")'
driver.execute_script(js)
time.sleep(2)
driver.quit()
