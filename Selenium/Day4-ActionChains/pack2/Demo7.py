import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/submitted-scripts/i-google-like-drag-drop/index.html")
time.sleep(2)
# get element
element_block1 = driver.find_element(By.XPATH,"//h1[normalize-space()='Block 1']")
element_block3 = driver.find_element(By.XPATH,"//h1[normalize-space()='Block 3']")
# create action chain object
time.sleep(2)
action = ActionChains(driver)
action.drag_and_drop(element_block1, element_block3).perform()
time.sleep(2)
driver.quit()