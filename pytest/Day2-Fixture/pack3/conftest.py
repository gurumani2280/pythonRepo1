import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    print(" this is setup runs before method")
    #global driver
    driver = webdriver.Chrome()
    yield driver
    print("this is tear down method which executes after setup")
    driver.quit()