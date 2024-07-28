from .base_page import BasePage
from .locators import MainPageLocator, LoginPageLocators
from selenium.common.exceptions import NoSuchElementException

class LoginPage(BasePage):
       
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "Not found login url."

    def should_be_login_form(self):
        try:
            login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        except NoSuchElementException:
            assert False, "Not found login form"

    def should_be_register_form(self):
        try:
            register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        except NoSuchElementException:
            assert False, "Not found register form."
