from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def visit(self, url):
        self.driver.get(url)

    def find(self, locator):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass 
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass 
        self.find(locator).click()

    def write(self, locator, text):
        self.find(locator).send_keys(text)

    def close_alert_if_present(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass
        