import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.usefixtures("init")
class TestLogin2:
    def testlogindemo2(self):
        lp=LoginPage(self.driver)
        lp.login("standard_user","secret_sauce")
        pp=ProductPage(self.driver)
        pp.logout()
        lp.confirmloginiconisdisplayed()
