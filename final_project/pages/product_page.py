import math
#наследование свойств базовой страницы из класса BasePage
from .base_page import BasePage

#наследование от ProductPageLocators
from .locators import ProductPageLocators

#создание класса "основная станица"
class ProductPage(BasePage):

    # метод для нахождения кнопки добавления товара в корзину
    def should_be_btn_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "btn_add_to_basket is not presented"

    # метод для добавления товара в корзину
    def add_product_to_basket(self):
        btn_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        btn_to_basket.click()

    #метод поиска сообщения об успешном добавлении в корзину
    def should_be_success_massage(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "сообщение о добавлении товара в корзину не получено"

