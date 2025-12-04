import allure
from pages.login_page import LoginPage

@allure.epic("E-Commerce Platform")
@allure.feature("Authentication")
@allure.story("Valid login")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_with_valid_user(driver):
    page = LoginPage(driver)
    page.load()
    page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

@allure.epic("E-Commerce Platform")
@allure.feature("Authentication")
@allure.story("Invalid user")
@allure.severity(allure.severity_level.NORMAL)
def test_login_with_invalid_user(driver):
    page = LoginPage(driver)
    page.load()
    page.login("wrong_user", "wrong_pass")
    assert "Epic sadface" in page.get_error_message()
    