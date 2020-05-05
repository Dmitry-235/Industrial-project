from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    URL_CORR = "/login/"
    FORM_LOG_IN = (By.ID, "login_form")
    FORM_REG = (By.ID, "register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, "button[name = registration_submit]")

class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    ALERT_ADDED_TO_CART = (By.CSS_SELECTOR, "div.alertinner strong")
    ALERT_CART_STATUS = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")
    PRICE_VALUE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")

    #Плюсы наследования: пример
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BUTTON_BASKET = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')