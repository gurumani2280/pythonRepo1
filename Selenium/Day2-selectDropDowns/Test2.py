from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///fullPath/BasicHtmlElement.html")
time.sleep(3)

numberdropdown = driver.find_element(By.NAME,'alloptions')
sel = Select(numberdropdown)
sel.select_by_index(3)
time.sleep(1)
sel.select_by_value("2")
time.sleep(1)
sel.select_by_visible_text("FIVE")
time.sleep(3)
sel.deselect_by_index(3)
time.sleep(2)
print(sel.is_multiple)
driver.quit()




