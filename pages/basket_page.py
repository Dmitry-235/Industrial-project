from .base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def guest_go_home_basket_wait(self):
        login_link = self.browser.find_element(*BasketPageLocators.BUTTON_BASKET)
        login_link.click()

