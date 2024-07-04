import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def init(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/v1/")
    request.cls.driver=driver
    yield
    driver.quit()