from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):

    COMPLETE_HEADER = (By.XPATH, "//h2[text()='Thank you for your order!']")

    def is_loaded(self):
        self.find(self.COMPLETE_HEADER)

    def success_message(self):
        return self.find(self.COMPLETE_HEADER).text
    