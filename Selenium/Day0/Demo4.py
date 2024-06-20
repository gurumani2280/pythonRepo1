from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/v1/")
time.sleep(2)
print("trying to identify the username element on the page")
username_element = driver.find_element(By.ID,"user-name")
if username_element is not None :
    print("the username is identified successfully")
    username_element.send_keys("standard_user")
time.sleep(3)

driver.quit()


'''there are 8 locators available inside selenium
1. ID
2.Name
3. Linktext
4.partiallinktext
5.CSSselector
6.xpath
7.classname
8.Tagname'''