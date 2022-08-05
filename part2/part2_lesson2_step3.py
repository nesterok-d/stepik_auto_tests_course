from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math



try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # код, который находит X
    x1_element = browser.find_element(By.ID, "num1")
    x2_element = browser.find_element(By.ID, "num2")
    x1 = x1_element.text
    x2 = x2_element.text
    # вычисляем функцию
    y = int(x1)+int(x2)
    # выбираем ответ
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(y))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла