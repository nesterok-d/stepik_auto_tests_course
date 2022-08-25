#создение класса "старница"

class BasePage():
    #создение метода инициализации объекта класса (конструктор)
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    #создение метода открывания страницы
    def open(self):
        self.browser.get(self.url)