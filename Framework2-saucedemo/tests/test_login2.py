import pytest

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
