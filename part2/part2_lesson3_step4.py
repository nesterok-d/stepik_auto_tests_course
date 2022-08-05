from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #жмем на кнопку
    button1 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button1.click()

    #переходим к alert
    alert = browser.switch_to.alert
    alert.accept()

    # код, который находит X
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    # вычисляем функцию
    y = calc(x)
    # заполняем поле с ответом
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла