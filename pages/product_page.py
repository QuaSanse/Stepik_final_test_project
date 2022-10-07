from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    'Страница товара'

    def should_be_product_page(self):
        self.go_add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.check_exists_messege_added_to_cart()
        self.check_of_the_product_name_in_the_message()
        self.check_price_message()

    def should_be_product_url(self):
        """ проверка на верный url адрес для промо"""
        assert '?promo=' in self.browser.current_url, "Current url does not contain product page"

    def go_add_product_to_basket(self):
        """ метод добавления товара в корзину """
        btn_add_to_basket = self.browser.find_element(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET)
        btn_add_to_basket.click()

    def check_exists_messege_added_to_cart(self):
        """ проверка на наличие сообщения о добавлении товара в корзину и цены"""
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSEGE), "there is no message about adding an item to the cart"
        assert self.is_element_present(
            *ProductPageLocators.PRICE_PRODUCT_IN_MESSEGE), "no price message in cart"

    def check_of_the_product_name_in_the_message(self):
        """ метод сравнения названия товара добавленного в корзину """
        product_name_on_page = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_ON_PAGE)
        product_name_in_messege = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSEGE)

        print(
            f'Товар "{product_name_in_messege.text}" добавлен в корзину')
        assert product_name_on_page.text == product_name_in_messege.text, f"Product name {product_name_on_page.text} does not match {product_name_in_messege.text}"

    def check_price_message(self):
        """ метод сравнения цен со страницы и после добавления """
        price_on_page = self.browser.find_element(
            *ProductPageLocators.PRICE_PRODUCT_ON_PAGE)
        price_on_messege = self.browser.find_element(
            *ProductPageLocators.PRICE_PRODUCT_IN_MESSEGE)

        assert price_on_page.text == price_on_messege.text, "Prices do not match"

        print(f'Стоимость корзины {price_on_messege.text}')

    def should_not_be_success_message(self):
        """ проверяет, что элемент не появляется на странице в течение заданного времени, если элемент находиться , тест падает """
        assert self.is_not_element_present(*ProductPageLocators.PRICE_PRODUCT_IN_MESSEGE), \
            "Success message is presented, but should not be"

    def the_success_message_should_disappear(self):
        """ проверяет, что элемент исчез со страницы в течение заданного времени, если элемент находиться , тест падает """
        assert self.is_disappeared(*ProductPageLocators.PRICE_PRODUCT_IN_MESSEGE), \
            "Success message should disappear, but didn't"
