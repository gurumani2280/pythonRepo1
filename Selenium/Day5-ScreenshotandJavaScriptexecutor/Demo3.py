import time
from selenium import webdriver
browser=webdriver.Chrome()
browser.get("https://en.wikipedia.org")
time.sleep(2)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
browser.execute_script("window.scrollTo(0,0)")
time.sleep(2)
browser.close()