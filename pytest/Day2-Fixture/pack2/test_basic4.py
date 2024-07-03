from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
@pytest.mark.multiplewindow
def test_basic5(setup):
    print("This is multiple window program")

    #driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.get("http://demo.automationtesting.in/Windows.html")
    parent_window_handle = driver.current_window_handle
    print("parent_window_handle ======", parent_window_handle)
    print("type(parent_window_handle) ======", type(parent_window_handle))

    all_window_handles = driver.window_handles
    print("all_window_handles ======", all_window_handles)
    print("type of all_window_handles ======", type(all_window_handles))

    # Opens a new tab and switches to new tab
    driver.switch_to.new_window('tab')
    time.sleep(3)
    # Opens a new window and switches to new window
    driver.switch_to.new_window('window')
    time.sleep(4)
    print("after opening a new tab or window")
    child_window_handle = driver.current_window_handle
    print("child_window_handle ======", child_window_handle)
    print("type(child_window_handle) ======", type(child_window_handle))

    all_window_handles = driver.window_handles
    print("all_window_handles ======", all_window_handles)
    print("type of all_window_handles ======", type(all_window_handles))
@pytest.fixture
def setup():
    print(" this is setup runs before method")
    global driver
    driver = webdriver.Chrome()
    yield
    print("this is tear down method which executes after setup")
    driver.quit()

