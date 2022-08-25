from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "input[id='id_login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[id='id_login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn-lg[name='login_submit']")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "input[id='id_registration-email']")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "input[id='id_registration-password1']")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "input[id='id_registration-password2']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button.btn-lg[name='registration_submit']")