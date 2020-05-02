from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_at_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET)
        basket_button.click()
        self.solve_quiz_and_get_code()

    def should_product_add_basket(self):
       #Дописать методы-проверки.
       assert self.is_element_present(*ProductPageLocators.ADD_IN_LINK), \
           "Button Add In Basket is not presented"