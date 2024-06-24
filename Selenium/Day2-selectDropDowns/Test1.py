from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///fullXpath/BasicHtmlElement.html")
time.sleep(3)

statedropdown = driver.find_element(By.NAME,'state')
sel = Select(statedropdown)
sel.select_by_index(3)
time.sleep(1)
sel.select_by_value("2")
time.sleep(1)
sel.select_by_visible_text("KARNATAKA")
time.sleep(3)
print(sel.is_multiple)
driver.quit()




