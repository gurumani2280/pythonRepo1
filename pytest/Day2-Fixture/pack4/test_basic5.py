from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
class TestFrame:
    @pytest.mark.frame
    def test_basic2(self,setup):
        driver = setup
        print("This is multiple frame program")

        driver.get("file:///E:/EMXO-python/pythonRepo1/Selenium/Demo2.html")
        time.sleep(2)
        driver.find_element(By.ID, "t1").send_keys("oldData")
        time.sleep(3)
        # switch to 1st frame
        driver.switch_to.frame(0)
        driver.find_element(By.ID, "t2").send_keys("someData")
        time.sleep(3)
        # back to default web page frame
        driver.switch_to.default_content()
        driver.find_element(By.ID, "t1").send_keys("newData")

        time.sleep(2)




