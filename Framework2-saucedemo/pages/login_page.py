from selenium.webdriver.common.by import By

from pages.login_page_locator import LoginPageLocator


class LoginPage(LoginPageLocator):
    def __init__(self,driver):
        self.driver=driver

    def get_username_locator(self):
        return self.driver.find_element(*self.username_locator)

    def get_password_locator(self):
        return self.driver.find_element(*self.password_locator)

    def get_login_locator(self):
        return self.driver.find_element(*self.login_locator)

    def get_loginsymbol_locator(self):
        return self.driver.find_element(*self.loginsymbol_locator)

    def login(self,username,password):
        self.get_username_locator().send_keys(username)
        self.get_password_locator().send_keys(password)
        self.get_login_locator().click()


    def confirmloginiconisdisplayed(self):
        self.get_loginsymbol_locator().is_displayed()




