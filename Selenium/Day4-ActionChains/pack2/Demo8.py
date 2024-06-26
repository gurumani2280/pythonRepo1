import time
from selenium import webdriver
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/index.htm")
time.sleep(3)
# get element
element = driver.find_element(By.XPATH,"//h5[text()='About us']")
# create action chain object
action = ActionChains(driver)

# put mouse on the web element
action.move_to_element(element)

# perform the operation
action.perform()
time.sleep(3)
driver.quit()
