import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import BasePageLocators
import time


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, *BasePageLocators.LOGIN_LINK)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, "ssswwee")
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_cart()
        page.check_for_message_product_is_add()
        page.check_for_correct_cart_price()

    @pytest.mark.two
    def test_user_cant_see_success_message(browser):
        product_page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        product_page.open()
        product_page.check_adding_message_not_present()


@pytest.mark.login
class TestLoginFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title="Best book created by robot")
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали
        self.product.delete()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста


@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url, 2)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_text_message()


@pytest.mark.guest1
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.guest2
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = BasePage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.one
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    product_page.open()
    product_page.add_product_to_cart()
    product_page.should_not_be_success_message()


@pytest.mark.three
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    product_page.open()
    product_page.add_product_to_cart()
    product_page.check_adding_message_is_disappeared()
