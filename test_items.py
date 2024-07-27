from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_different_languages(browser):
    browser.get(link)
    time.sleep(10)
    btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-add-to-basket")))
    lang = browser.find_element(By.CLASS_NAME, 'no-js').get_attribute('lang')
    # print(lang, 'where')
    if lang == 'fr':
        assert btn.text == 'Ajouter au panier'