from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    FORM_LOGIN = (By.CSS_SELECTOR, "form#login_form")
    FORM_REGISTER = (By.CSS_SELECTOR, "form#register_form")
