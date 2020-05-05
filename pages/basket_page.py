from .base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def guest_go_home_basket_wait(self):
        login_link = self.browser.find_element(*BasketPageLocators.BUTTON_BASKET)
        login_link.click()

    def should_be_home_basket_link(self):
        assert self.is_element_present(*BasketPageLocators.BUTTON_BASKET), \
            "Basket link is not presented"