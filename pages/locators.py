from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    URL_CORR = "/login/"
    FORM_LOG_IN = (By.ID, "login_form")
    FORM_REG = (By.ID, "register_form")

class ProductPageLocators():
    ADD_IN_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADD_IN_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")

