from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
import pytest, time

product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
product_link_without_promo = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.skip
def test_should_be_promo_product_page(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_promo_product_page()


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                      pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

    

        
# @pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_link_without_promo)
    product_page.open()
    product_page.message_disappeared_after_adding_product_to_basket()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()   
    # page.guest_can_add_product_to_basket()
    page.go_to_basket_page()
    page.should_be_basket_is_empty()
    
class TestUserAddToBasketFromProductPage():    
    @pytest.mark.skip
    def test_user_can_add_product_to_basket(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.guest_can_add_product_to_basket()
        product_page.should_be_product_in_the_basket()

    # @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, product_link_without_promo)
        product_page.open()
        product_page.guest_cant_see_success_message_after_adding_product_to_basket()

    # @pytest.mark.xfail
    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, product_link_without_promo)
        product_page.open()
        product_page.guest_cant_see_success_message()