from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class ProductPage:
    def __init__(self,driver):
        self.driver=driver

    def logout(self):
        homepage_openmenu = self.driver.find_element(By.CSS_SELECTOR, "div.bm-burger-button")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of(homepage_openmenu))
        assert homepage_openmenu.is_displayed(), "open menu is not displayed"
        homepage_openmenu.click()
        logout_menu = self.driver.find_element(By.XPATH, "//a[text()='Logout']")
        wait.until(expected_conditions.visibility_of(logout_menu))
        assert logout_menu.is_displayed()
        logout_menu.click()