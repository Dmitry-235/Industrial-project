import pytest

from pages.basket_page import BasketPage
from pages.product_page import ProductPage

link = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"]

@pytest.mark.parametrize("link", link)
@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser, link: str) -> None:
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart(True)
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()

@pytest.mark.parametrize("link", link)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link: str) -> None:
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
