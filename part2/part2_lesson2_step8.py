from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import math



try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname('TestText.txt'))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'TestText.txt')

    firstName = browser.find_element(By.CSS_SELECTOR, "div.form-group input[name='firstname']")
    lastName = browser.find_element(By.CSS_SELECTOR, "div.form-group input[name='lastname']")
    email = browser.find_element(By.CSS_SELECTOR, "div.form-group input[name='email']")

    firstName.send_keys("Иван")
    lastName.send_keys("Иванов")
    email.send_keys("ivanov.i@gmail.com")

    element = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
