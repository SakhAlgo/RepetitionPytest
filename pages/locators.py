from selenium.webdriver.common.by import By

class MainPageLocator():
    LOGIN_LOCATOR = (By.CSS_SELECTOR, '#login_link')
    CATALOG_LOCATOR = (By.CSS_SELECTOR, '.dropdown > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)')

class BasketPageLocator():
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p") 
    BASKET_FULL = (By.CSS_SELECTOR, "#content_inner > article")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LOCATOR = (By.CSS_SELECTOR, '.btn-group > a:nth-child(1)')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form1')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '#register_form > button:nth-child(7)')
    
class ProductPageLocator():
    BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_NAME_IN_THE_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner > strong')
    MESSAGE_AFTER_ADDING_PRODUCT = (By.CSS_SELECTOR, 'div.alertinner ')
    FIRST_PRODUCT = (By.CSS_SELECTOR, 'img.thumbnail')
    