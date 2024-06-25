from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
#launch URL
driver.get("https://the-internet.herokuapp.com/jqueryui/menu#")
#object of ActionChains
a = ActionChains(driver)
#identify element
m = driver.find_element(By.LINK_TEXT,"Enabled")
#hover over element
a.move_to_element(m).perform()
#identify sub menu element
n = driver.find_element(By.LINK_TEXT,"Back to JQuery UI")
# hover over element and click
a.move_to_element(n).click().perform()
print("Page title: " + driver.title)


#n1 = driver.find_element(By.LINK_TEXT,"Downloads")
# hover over element and click
#a.move_to_element(n1).perform()


#n2 = driver.find_element(By.LINK_TEXT,"PDF")
# hover over element and click
#a.move_to_element(n2).click().perform()



print("Page title: " + driver.title)
#close browser
driver.quit()

