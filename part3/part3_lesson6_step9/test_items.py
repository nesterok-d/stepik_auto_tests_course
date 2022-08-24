from selenium.webdriver.common.by import By
import time



def test_btn_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

    assert button.text is not None, "кнопка купить отсутствует"
    time.sleep(20)
