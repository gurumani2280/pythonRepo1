import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    print(" this is setup runs before method")
    #global driver
    driver = webdriver.Chrome()
    request.cls.driver=driver
    yield
    print("this is tear down method which executes after setup")
    driver.quit()