from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/v1/")
driver.find_element(By.NAME,"user-name").send_keys("standard_user")
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
homepage_openmenu = driver.find_element(By.CSS_SELECTOR,"div.bm-burger-button")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of(homepage_openmenu))
assert homepage_openmenu.is_displayed(),"open menu is not displayed"
homepage_openmenu.click()
logout_menu = driver.find_element(By.XPATH,"//a[text()='Logout']")
wait.until(expected_conditions.visibility_of(logout_menu))
assert logout_menu.is_displayed()
logout_menu.click()
driver.find_element(By.XPATH,"//img[@src='img/Login_Bot_graphic.png']").is_displayed()
driver.quit()