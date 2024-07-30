from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
import pytest, time
from .pages.login_page import LoginPage
from .pages.locators import BasePageLocators, MainPageLocator, ProductPageLocator
import faker
fk = faker.Faker()

product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
product_link_without_promo = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.skip
# @pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, product_link_without_promo):
    product_page = ProductPage(browser, product_link_without_promo)
    product_page.open()
    product_page.guest_can_add_product_to_basket()
    product_page.should_be_product_in_the_basket()

# @pytest.mark.skip
@pytest.mark.need_review
def test_should_be_promo_product_page(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_promo_product_page()
      
# @pytest.mark.xfail
@pytest.mark.skip
@pytest.mark.need_review
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_link_without_promo)
    product_page.open()
    product_page.message_disappeared_after_adding_product_to_basket()

# @pytest.mark.skip
@pytest.mark.need_review
def test_guest_can_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()   
    page.go_to_basket_page()
    page.should_be_basket_is_empty()


class TestUserAddToBasketFromProductPage():   
    def register_new_user_and_came_back(self, browser):
        product_page = ProductPage(browser, url=product_link_without_promo)
        product_page.open()
        # получаем форму регисрации и регестрируемся      
        login_elem = browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_elem.click()        
        product_page.register_new_user(email=fk.email(), password='!@#$qwaszx')
        
        # переходим в каталог
        login_elem = browser.find_element(*MainPageLocator.CATALOG_LOCATOR)
        login_elem.click()
        return product_page

    # @pytest.mark.skip    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = self.register_new_user_and_came_back(browser)
        
        # кликаем по первой позиции товара 
        login_elem = browser.find_element(*ProductPageLocator.FIRST_PRODUCT)
        login_elem.click()
        
        product_page.guest_can_add_product_to_basket()
        product_page.should_be_product_in_the_basket()

    # @pytest.mark.xfail
    # @pytest.mark.skip
    @pytest.mark.need_review
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_page = self.register_new_user_and_came_back(browser) 
        
        # кликаем по первой позиции товара 
        login_elem = browser.find_element(*ProductPageLocator.FIRST_PRODUCT)
        login_elem.click()       

        time.sleep(2)
        product_page.guest_can_see_success_message_after_adding_product_to_basket()

    # @pytest.mark.xfail
    # @pytest.mark.skip
    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        product_page = self.register_new_user_and_came_back(browser) 
        
        # кликаем по первой позиции товара 
        login_elem = browser.find_element(*ProductPageLocator.FIRST_PRODUCT)
        login_elem.click()   
        
        product_page.guest_cant_see_success_message()