from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutStepOnePage(BasePage):

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_INPUT = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    def is_loaded(self):
        self.find(self.FIRST_NAME_INPUT)

    def fill_info(self, first, last, zip_code):
        self.type(self.FIRST_NAME_INPUT, first)
        self.type(self.LAST_NAME_INPUT, last)
        self.type(self.ZIP_INPUT, zip_code)

    def continue_checkout(self):
        self.click(self.CONTINUE_BTN)
