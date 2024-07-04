from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    def login(self,username,password):
        self.driver.find_element(By.NAME, "user-name").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def confirmloginiconisdisplayed(self):
        self.driver.find_element(By.XPATH, "//img[@src='img/Login_Bot_graphic.png']").is_displayed()




