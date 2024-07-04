import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
@pytest.mark.usefixtures("init")
class TestLogin:
    def testlogindemo(self):
        self.driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        homepage_openmenu = self.driver.find_element(By.CSS_SELECTOR, "div.bm-burger-button")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of(homepage_openmenu))
        assert homepage_openmenu.is_displayed(), "open menu is not displayed"
        homepage_openmenu.click()
        logout_menu = self.driver.find_element(By.XPATH, "//a[text()='Logout']")
        wait.until(expected_conditions.visibility_of(logout_menu))
        assert logout_menu.is_displayed()
        logout_menu.click()
        self.driver.find_element(By.XPATH, "//img[@src='img/Login_Bot_graphic.png']").is_displayed()
