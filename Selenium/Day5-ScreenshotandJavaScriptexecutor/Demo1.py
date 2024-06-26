from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window();
driver.get('https://pythonspot.com')
driver.save_screenshot("screenshot.png")
#driver.get_screenshot_as_file("screenshot3.png")

element = driver.find_element(By.CSS_SELECTOR, 'div.head')
element.screenshot('just-the-header.png')
driver.close()
