import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--user_language') #, action='store', default=None, help="Choose language: es or ru"

@pytest.fixture()
def browser(request):
    user_language = request.config.getoption("user_language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()
