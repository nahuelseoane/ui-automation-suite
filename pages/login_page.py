from selenium.webdriver.common.by import By
from .base_page import BasePage
import config

class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN  = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def load(self):
        self.visit(config.BASE_URL)
    
    def login(self, username, password):
        self.write(self.USERNAME, username)
        self.write(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

        self.close_alert_if_present()
    
    def get_error_message(self):
        return self.find(self.ERROR_MSG).text
    