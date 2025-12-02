from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutStepTwoPage(BasePage):

    SUMMARY_TITLE = (By.XPATH, "//span[text()='Checkout: Overview']")
    FINISH_BTN = (By.ID, "finish")

    def is_loaded(self):
        self.find(self.SUMMARY_TITLE)

    def finish_order(self):
        self.click(self.FINISH_BTN)
