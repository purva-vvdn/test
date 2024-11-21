import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
import time


@pytest.fixture(scope="class")
def setup(request):
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)

    # Navigate to the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    # Perform login using LoginPage object
    login_driver = LoginPage(driver)
    time.sleep(2)
    login_driver.enter_username("Admin")
    login_driver.enter_password("admin123")
    login_driver.enter_button()
    time.sleep(3)

    # Assign driver to the test class
    request.cls.driver = driver
    yield
    driver.quit()