from selenium.webdriver.common.by import By

class MainPageLocator():
    LOGIN_LOCATOR = (By.CSS_SELECTOR, '#login_link')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form1')    
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form1')    
    
class ProductPageLocator():
    BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_NAME_IN_THE_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner > strong')
    MESSAGE_AFTER_ADDING_PRODUCT = (By.CSS_SELECTOR, 'div.alertinner ')