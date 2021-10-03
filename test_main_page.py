import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):  # подготовка к тестам (preconditions)
        print('Start test')
        self.link = "http://selenium1py.pythonanywhere.com/"
        # манипуляции с браузером в сетапе для примера. Это делать не рекомендуется
        # здесь, например, можно создать пользователя по API
        self.page = MainPage(browser, self.link)
        self.page.open()
        yield
        # а здесь уже удалить пользователя, тоже по API
        print('\nEnd test')

    def test_guest_can_go_to_login_page(self, browser):
        self.page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.should_be_login_form()

    def test_guest_should_see_login_link(self):
        self.page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.empty_message_is_present()
