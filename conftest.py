import os
import shutil
import allure
from allure_commons.types import AttachmentType
import pytest
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    temp_dir = tempfile.mkdtemp()
    user_data_dir = os.path.join(temp_dir, "chrome-data")
    options = Options()
    
    options.add_argument("--headless=new")
    options.add_argument("--incognito")

    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument("--start-maximized")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-features=PasswordLeakDetection,AutofillServerCommunication")
    options.add_argument("--disable-save-password-bubble")
    

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "password_manager_leak_detection.enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False,
        "autofill.address_enabled": False
    })

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)


    yield driver
    driver.quit()
    shutil.rmtree(temp_dir, ignore_errors=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=AttachmentType.PNG
            )