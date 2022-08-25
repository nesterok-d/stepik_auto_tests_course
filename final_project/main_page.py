#наследование свойств базовой страницы из класса BasePage
from .base_page import BasePage

from selenium.webdriver.common.by import By

#создание класса "основная станица"
class MainPage(BasePage):
    #создание метода для пеерхода к странице логина
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()