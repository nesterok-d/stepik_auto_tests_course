from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 15 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    buttonBook = browser.find_element(By.ID, "book")
    buttonBook.click()

    # код, который находит X
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    # вычисляем функцию
    y = calc(x)
    # заполняем поле с ответом
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)


    # Отправляем заполненную форму
    #button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1 = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла