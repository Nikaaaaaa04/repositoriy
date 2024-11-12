import time
from selenium.webdriver.common.by import By

def test_add_to_cart_button(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    time.sleep(30)  # Визуальная проверка кнопки
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button is not None  # Проверяем, что кнопка существует
