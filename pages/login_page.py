from .base_page import BasePage
from .locators import MainPageLocator, LoginPageLocators
from selenium.common.exceptions import NoSuchElementException
import pytest
import faker
import time


fk = faker.Faker()

class LoginPage(BasePage):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.register_new_user()
    
    def register_new_user(self, email=fk.email(), password='!@#$qwaszx'):
        try:
            reg_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
            reg_password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
            reg_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
            reg_email.send_keys(email)
            reg_password1.send_keys(password)
            reg_password2.send_keys(password)
            
            time.sleep(2)
            btn_reg = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
            btn_reg.click()
            self.should_be_authorized_user()
            
        except NoSuchElementException:
            assert False, "Not found login form"
       
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
