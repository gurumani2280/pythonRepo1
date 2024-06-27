import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
parent_window_handle = driver.current_window_handle
print("parent_window_handle ======", parent_window_handle)
print("type(parent_window_handle) ======", type(parent_window_handle))

time.sleep(2)

driver.find_element(By.XPATH, '//div[@id="Tabbed"]/a/button').click()
time.sleep(2)
all_window_handles = driver.window_handles
print("all_window_handles ======", all_window_handles)

for window_handle in all_window_handles:
    if window_handle != parent_window_handle:
        child_window_handle = window_handle
        print("captured child window handle", child_window_handle)

driver.switch_to.window(child_window_handle)
driver.find_element(By.XPATH,"//span[text()='Documentation']").click()
time.sleep(3)

driver.quit()
