from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_no_items_in_the_cart(self):
        """ Ожидаем, что в корзине нет товаров """
        self.check_exists_massage_empty_cart()
        self.check_exists_form_items_in_the_cart()

    def check_exists_massage_empty_cart(self):
        """ проверка что есть текст о том что корзина пуста """
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_CART_MESSAGE), "no empty cart message"

    def check_exists_form_items_in_the_cart(self):
        """ проверка наличия формы добавленных товаров """
        assert self.is_not_element_present(*BasketPageLocators.FORM_ITEMS_IN_THE_CART), \
            "Success form is presented, but should not be"
