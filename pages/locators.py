from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    LOGIN_LINK = (By.ID, 'login_link')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form')
    PRODUCT_NAME = (By.CSS_SELECTOR, '[class="col-sm-6 product_main"] h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    NAME_IN_CART = (By.CSS_SELECTOR, '.alertinner strong')
    PRICE_IN_CART = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner ')
