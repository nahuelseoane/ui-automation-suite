import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutStepOnePage(BasePage):

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_INPUT = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    @allure.step("Verifying checkout step one is loaded")
    def is_loaded(self):
        self.find(self.FIRST_NAME_INPUT)

    @allure.step("Filling checkout information: {first} {last}, ZIP: {zip_code}")
    def fill_info(self, first, last, zip_code):
        self.write(self.FIRST_NAME_INPUT, first)
        self.write(self.LAST_NAME_INPUT, last)
        self.write(self.ZIP_INPUT, zip_code)

    @allure.step("Continuing to checkout step two")
    def continue_checkout(self):
        self.click(self.CONTINUE_BTN)
