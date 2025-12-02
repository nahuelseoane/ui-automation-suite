from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_step1_page import CheckoutStepOnePage
from pages.checkout_step2_page import CheckoutStepTwoPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_checkout_flow(driver):
    # Login
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    # Inventory
    inventory = InventoryPage(driver)
    inventory.is_loaded()
    inventory.add_backpack_to_cart()

    # Go to cart
    driver.get("https://www.saucedemo.com/cart.html")
    cart = CartPage(driver)
    cart.is_loaded()
    cart.go_to_checkout()

    # Checkout Step 1
    step1 = CheckoutStepOnePage(driver)
    step1.is_loaded()
    step1.fill_info("Nahuel", "Seoane", "1706")
    step1.continue_checkout()

    # Checkout Step 2
    step2 = CheckoutStepTwoPage(driver)
    step2.is_loaded()
    step2.finish_order()

    # Checkout Complete
    complete = CheckoutCompletePage(driver)
    complete.is_loaded()
    assert complete.success_message() == "Thank you for your order!"
    