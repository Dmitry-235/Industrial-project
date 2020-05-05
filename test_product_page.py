from datetime import time

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.page = LoginPage(browser, link)
        self.page.open()
        email = str(time.time()) + "@email.ru"
        password = str(time.time())
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(browser: str) -> None:
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_cart(True)
        product_page.should_be_present_in_cart()
        product_page.should_check_overall_cost()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser: str) -> None:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart(True)
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()

def test_guest_can_add_non_promo_product_to_cart(browser) -> None:
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()

    #Плюсы наследования: пример
@pytest.mark.need_review
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = BasketPage(browser, link)
    page.open()
    page.guest_go_home_basket_wait()

def test_should_see_product_basket_at_home_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_home_basket_link()