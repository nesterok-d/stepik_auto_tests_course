#создение класса "старница"

class BasePage():
    #создение метода инициализации объекта класса (конструктор)
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    #создение метода открывания страницы
    def open(self):
        self.browser.get(self.url)