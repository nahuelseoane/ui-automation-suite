import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@allure.feature("Shopping Cart")
@allure.story("Add Item to Cart")
def test_add_item_to_cart(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user","secret_sauce")

    inventory = InventoryPage(driver)
    inventory.close_alert_if_present()
    inventory.is_loaded()

    inventory.add_backpack_to_cart()
    assert inventory.get_cart_count() == 1

@allure.feature("Shopping")
@allure.story("Remove Item from Cart")
def test_remove_item_from_cart(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.is_loaded()

    inventory.add_backpack_to_cart()
    inventory.remove_backpack_from_cart()
    assert inventory.get_cart_count() == 0
