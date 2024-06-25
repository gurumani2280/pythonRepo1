import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(1)
# get element
element = driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']")
# create action chain object
action = ActionChains(driver)
action.double_click(element).perform()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
driver.quit()