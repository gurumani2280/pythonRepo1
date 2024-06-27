import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
parent_window_handle = driver.current_window_handle
print("parent_window_handle ======", parent_window_handle)

all_window_handles = driver.window_handles
print("all_window_handles ======", all_window_handles)

# Opens a new tab and switches to new tab
#driver.switch_to.new_window('tab')

# Opens a new window and switches to new window
driver.switch_to.new_window('window')
time.sleep(2)
print("after opening a new tab or window")
child_window_handle = driver.current_window_handle
print("child_window_handle ======", child_window_handle)

all_window_handles = driver.window_handles
print("all_window_handles ======", all_window_handles)

driver.get("https://www.selenium.dev/documentation/webdriver/interactions/windows/")
driver.close()
time.sleep(2)

driver.switch_to.window(parent_window_handle)
driver.find_element(By.XPATH, '//div[@id="Tabbed"]/a/button').click()
time.sleep(2)

driver.quit()
