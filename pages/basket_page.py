from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def empty_message_is_present(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), 'Empty basket message not found'

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket is not empty'
