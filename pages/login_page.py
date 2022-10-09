import time
from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """ метод проверку на url адрес login """
        assert 'login' in self.browser.current_url, "Current url does not contain login"

    def should_be_login_form(self):
        """ метод проверки что форма логина отображается """
        assert self.is_element_present(
            *LoginPageLocators.FORM_LOGIN), "There is no login form on the current page"

    def should_be_register_form(self):
        """ метод проверки что форма регистрации отображается """
        assert self.is_element_present(
            *LoginPageLocators.FORM_REGISTER), "There is no register form on the current page"

    def register_new_user(self, email, password):
        """ метод регистрации пользователя """
        # вводим email
        input_email = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        input_email.clear()
        input_email.send_keys(email)

        # вводим password
        input_password1 = self.browser.find_element(
            *LoginPageLocators.INPUT_PASSWORD1)
        input_password1.clear()
        input_password1.send_keys(password)

        # вводим повторно password
        input_password2 = self.browser.find_element(
            *LoginPageLocators.INPUT_PASSWORD2)
        input_password2.clear()
        input_password2.send_keys(password)

        # жмем на кнопку подтверждения регистрации
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()

