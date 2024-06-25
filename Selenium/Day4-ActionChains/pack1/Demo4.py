import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# https://stackoverflow.com/questions/18026391/selenium-webdriver-in-python-files-download-directory-change-in-chrome-prefere
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
prefs = {"profile.default_content_settings.popups": 0,

            "download.default_directory": r"C:\Users\user_dir\Desktop\\", # IMPORTANT - ENDING SLASH V IMPORTANT
                "directory_upgrade": True}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(5)
# launch URL
driver.get("https://the-internet.herokuapp.com/jqueryui/menu#")
# object of ActionChains
a = ActionChains(driver)
# identify element
m = driver.find_element(By.LINK_TEXT, "Enabled")
# hover over element
a.move_to_element(m).perform()
# identify sub menu element
n = driver.find_element(By.LINK_TEXT, "Back to JQuery UI")

n1 = driver.find_element(By.LINK_TEXT, "Downloads")
# hover over element and click
a.move_to_element(n1).perform()

n2 = driver.find_element(By.LINK_TEXT, "PDF")
# hover over element and click
a.move_to_element(n2).click().perform()

print("Page title: " + driver.title)
time.sleep(5)
# close browser
driver.quit()
