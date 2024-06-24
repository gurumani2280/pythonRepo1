from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.implicitly_wait(20)
driver.maximize_window()
# Click the button to activate(generate) the alert
alert_button_locator = (By.XPATH, "//button[text()='Click for JS Alert']")
driver.find_element(*alert_button_locator).click()
# get the alert object
alert = driver.switch_to.alert
alert_text = alert.text
print("alert text == ", alert_text)
# Press the OK button
alert.accept()
result_locator = (By.CSS_SELECTOR, 'p#result')
result_element = driver.find_element(*result_locator)
result_text = result_element.text.strip()
print("result_text == ", result_text)
expected_text = 'You successfully clicked an alert'
failure_message = f"result text {result_text} not matching {expected_text}"
assert result_text == expected_text, failure_message
time.sleep(2)
driver.quit()
