import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
parent_window_handle = driver.current_window_handle
print("parent_window_handle ======", parent_window_handle)

all_window_handles = driver.window_handles
print("all_window_handles ======", all_window_handles)
time.sleep(2)

driver.find_element(By.XPATH, '//div[@id="Tabbed"]/a/button').click()
time.sleep(2)
print("after opening a new tab or window")
parent_window_handle_again = driver.current_window_handle
print("child_window_handle ======", parent_window_handle_again)

all_window_handles = driver.window_handles
print("all_window_handles ======", all_window_handles)

driver.quit()
