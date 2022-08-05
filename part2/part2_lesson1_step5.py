from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # код, который находит X
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    # вычисляем функцию
    y = calc(x)
    # заполняем поле с ответом
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    # отмечаем чек-бокс
    option1 = browser.find_element(By.CSS_SELECTOR, "[class='form-check-input']")
    option1.click()
    # выбираем радиобатн
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option1.click()
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла