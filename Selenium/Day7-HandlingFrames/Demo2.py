
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com")
driver.find_element(By.LINK_TEXT, "Frames").click()
driver.find_element(By.LINK_TEXT,"Nested Frames").click()
# to switch to frame with frame name
driver.switch_to.frame("frame-bottom")
# to get the text inside the frame and print on console
print(driver.find_element(By.XPATH,"//body").text)
# to move out the current frame to the page level
driver.switch_to.default_content()
#to close the browser
driver.quit()