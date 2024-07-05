import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--Browser", action="store", default="chrome", help="my option: Edge or firefox"
    )

@pytest.fixture(scope="class")
def init(request):
    browser = request.config.getoption("--Browser")
    print("==============", browser)
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/v1/")
    request.cls.driver=driver
    yield
    driver.quit()