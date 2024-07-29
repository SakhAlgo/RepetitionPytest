from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time

main_link = "http://selenium1py.pythonanywhere.com/"

def test_quest_go_to_login_page(browser):
    page = MainPage(browser, main_link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

def test_should_be_login_link(browser):
    page = MainPage(browser, main_link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()