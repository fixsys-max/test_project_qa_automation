from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def is_matching_product_name(self):
        product_name_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.NAME_IN_CART).text
        assert product_name_on_page == product_name_in_cart, 'Product name does not match'

    def is_matching_price(self):
        price_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_cart = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART).text
        assert price_on_page == price_in_cart, 'Price does not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but should not be'

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message did not disappear after'
