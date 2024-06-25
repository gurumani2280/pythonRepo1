import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(3)
# get element
element = driver.find_element(By.XPATH,"//span[text()='right click me']")
# create action chain object
action = ActionChains(driver)
action.context_click(element).perform()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='Copy']").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
driver.quit()