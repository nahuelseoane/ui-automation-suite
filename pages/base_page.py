import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Visiting URL: {url}")
    def visit(self, url):
        self.driver.get(url)

    @allure.step("Finding element: {locator}")
    def find(self, locator):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass 
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Clicking element: {locator}")
    def click(self, locator):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass 
        self.find(locator).click()

    @allure.step("Typing '{text}' into element: {locator}")
    def write(self, locator, text):
        self.find(locator).send_keys(text)

    def close_alert_if_present(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        