import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_busket_button(browser):
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')

    time.sleep(15)