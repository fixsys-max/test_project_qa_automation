import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


links_list = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
              pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                           marks=pytest.mark.xfail),
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


# 10 запусков с сылками из links_list
@pytest.mark.need_review
@pytest.mark.parametrize('link', links_list)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.is_matching_product_name()
    page.is_matching_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.empty_message_is_present()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.link = 'https://selenium1py.pythonanywhere.com/accounts/login/'
        self.email = str(time.time()) + "@testmail.org"
        self.password = 'Qwerty123@'
        self.login_page = LoginPage(browser, self.link)
        self.login_page.open()
        self.login_page.go_to_login_page()
        self.login_page.register_new_user(self.email, self.password)
        self.login_page.should_be_authorized_user()
        yield  # В данном случае это не обязательно, т.к. почистить бд от юзера не можем
        print(f'\nI want to delete user {self.email}, but I can\'t')

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.is_matching_product_name()
        page.is_matching_price()
