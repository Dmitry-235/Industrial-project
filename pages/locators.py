from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    URL_CORR = "/loggin/"
    FORM_LOG_IN = (By.ID, "login_form")
    FORM_REG = (By.ID, "register_form")


