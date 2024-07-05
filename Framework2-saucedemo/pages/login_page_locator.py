from selenium.webdriver.common.by import By

class LoginPageLocator:
    username_locator=(By.NAME, "user-name")
    password_locator=(By.NAME, "password")
    login_locator=(By.ID, "login-button")
    loginsymbol_locator=(By.XPATH, "//img[@src='img/Login_Bot_graphic.png']")
