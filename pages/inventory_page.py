from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):

    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    ADD_BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK_BTN = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def is_loaded(self):
        return self.find(self.INVENTORY_CONTAINER)

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BTN)

    def remove_backpack_from_cart(self):
        import time
        time.sleep(2)
        self.click(self.REMOVE_BACKPACK_BTN)

    def get_cart_count(self):
        try:
            return int(self.find(self.CART_BADGE).text)
        except:
            return 0
    
    def go_to_cart(self):
        self.click(self.CART_LINK)
        