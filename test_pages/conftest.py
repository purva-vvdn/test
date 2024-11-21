import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from pages.create_account_page import LoginPage


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    url = "https://accounts2-stg.netgear.com/login?redirectUrl=https:%2F%2Fmaint-beta.insight.netgear.com%2F&clientId=454f9lfekd240pu1kdfpqth9fg"
    driver.get(url)
    driver.maximize_window()
    sleep(5)
    request.cls.driver = driver
    yield
    driver.quit()