from .pages.login_page import LoginPage
import pytest, time


def test_register_new_user(browser):
    login_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(browser, login_link)
    page.open()
    page.register_new_user()