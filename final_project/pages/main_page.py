#наследование свойств базовой страницы из класса BasePage
from .base_page import BasePage

#наследование от MainPageLocators
from .locators import MainPageLocators

#создание класса "основная станица"
class MainPage(BasePage):

    # создание метода для поиска ссылка на логин
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    #создание метода для пеерхода к странице логина
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()