import time

#наследуем методы из класса MainPage
from final_project.pages.product_page import ProductPage



#создаем тестовые сцениарии

#поиск ссылки на страницу логина
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(5)
    page.should_be_btn_add_to_basket()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_massage()
    time.sleep(5)
