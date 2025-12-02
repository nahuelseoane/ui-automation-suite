from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    CART_TITLE = (By.XPATH, "//span[text()='Your Cart']")
    CHECKOUT_BTN = (By.ID, "checkout")

    def is_loaded(self):
        self.find(self.CART_TITLE)

    def go_to_checkout(self):
        self.click(self.CHECKOUT_BTN)
        