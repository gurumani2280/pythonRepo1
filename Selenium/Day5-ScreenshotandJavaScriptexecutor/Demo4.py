from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://reddit.com")
cookies = browser.get_cookies()
for cookie in cookies:
    print(cookie)

browser.quit()