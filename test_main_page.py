from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.locators import BasketPageLocator
import time
import pytest

main_link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_quest
class TestLoginFormMainPage():    
    def test_quest_go_to_login_page(self, browser):
        page = MainPage(browser, main_link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()
        

    def test_quest_should_be_login_link(self, browser):
        page = MainPage(browser, main_link)
        page.open()
        page.should_be_login_link()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, main_link)
    page.open()
    page.go_to_basket_page()
    page.should_be_basket_is_empty()
