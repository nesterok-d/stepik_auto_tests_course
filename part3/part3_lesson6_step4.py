import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def browser():
    # print("\n start browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # print("\n quit browser..")
    browser.quit()


  #, "236896", "236897", "236898", "236899", "236903", "236904", "236905"
class TestMainPage1():

    @pytest.mark.parametrize('num', ["236895"])
    def test_guest_should_see_login_link(self, browser, num):
        link = "https://stepik.org/lesson/" + num + "/step/1"
        browser.get(link)
        time.sleep(5)

        answerFild = browser.find_element(By.CSS_SELECTOR, "textarea")
        answer = math.log(int(time.time()))

        answerFild.send_keys(answer)
        browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
        feedBack = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
        feedBackText = feedBack.text
        assert feedBackText == "Correct!"

if __name__ == "__main__":
    unittest.main()