from locators.login_page_locators import *
import time
class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,username):
        self.driver.find_element(*login_username).send_keys(username)
        time.sleep(2)

    def enter_password(self,password):
        self.driver.find_element(*login_password).send_keys(password)
        time.sleep(2)

    def enter_button(self):
        self.driver.find_element(*click_button).click()
        time.sleep(5)