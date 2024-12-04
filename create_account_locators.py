from selenium.webdriver.common.by import By


# username = By.XPATH, '//input[@id="mat-input-0"]'
# password = By.XPATH, '//input[@id="mat-input-1"]'
# login = By.XPATH, '//span[text()="NETGEAR Sign In"]'

create_another_account = By.XPATH, "//a[text()=' Create an Account ']"
email_address = By.XPATH, '//input[@formcontrolname="email"]'
confirm_email_address1 = By.ID, "lbl_cnfEmail"
confirm_email_address = By.ID, 'cnfEmail'
enter_name = By.ID, 'ip_firstName'
enter_last_name = By.ID, 'ip_lastName'
enter_password  = By.ID, 'ip_pwdSignup'
confirm_password = By.ID, 'ip_cnfPwd'
selecting_country = By.ID, 'id="mat-input-6"'
country_India = By.XPATH, '//select/option[text()=" United States "]'
clicking_on_checkbox = By.ID, "mat-mdc-checkbox-1-input"
clicking_on_next = By.XPATH, '//button[@form="signupForm"]'
# name_locator = By.XPATH, '//input[@id="ip_firstName"]'
wrong_email_error_text = By.XPATH, '//mat-error'



