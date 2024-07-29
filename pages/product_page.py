from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocator
from selenium.common.exceptions import NoAlertPresentException # в начале файла
# import math
import time

class ProductPage(BasePage):
    def should_be_promo_product_page(self):
        assert  "?promo=" in self.url, 'Not promo in the link.'
        
    def guest_can_add_product_to_basket(self):
        btn_basket = self.browser.find_element(*ProductPageLocator.BASKET_BUTTON)
        btn_basket.click()
        # time.sleep(3)
        self.solve_quiz_and_get_code()
    
    def should_be_product_in_the_basket(self):
        product_name = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME).text
        product_name_in_the_basket = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME_IN_THE_MESSAGE).text
        # print(product_name, product_name_in_the_basket)
        assert product_name == product_name_in_the_basket, 'There is not product in the basket'
        
    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.guest_can_add_product_to_basket()
        assert self.is_not_element_present(*ProductPageLocator.MESSAGE_AFTER_ADDING_PRODUCT), 'Messge is absent Test1'
        
    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocator.MESSAGE_AFTER_ADDING_PRODUCT), 'Messge is absent Test2'     

    def message_disappeared_after_adding_product_to_basket(self):
        self.guest_can_add_product_to_basket()
        assert self.is_disappeared(*ProductPageLocator.MESSAGE_AFTER_ADDING_PRODUCT), 'Messge is not disappeared Test3'
        
