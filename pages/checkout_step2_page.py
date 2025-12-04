import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutStepTwoPage(BasePage):

    SUMMARY_TITLE = (By.XPATH, "//span[text()='Checkout: Overview']")
    FINISH_BTN = (By.ID, "finish")

    @allure.step("Verifying checkout step two is loaded")
    def is_loaded(self):
        self.find(self.SUMMARY_TITLE)

    @allure.step("Finishing the order")
    def finish_order(self):
        self.click(self.FINISH_BTN)

    @allure.step("Getting order total")
    def get_total(self):
        return self.find(self.TOTAL_LABEL).text
