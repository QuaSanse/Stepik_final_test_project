from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    'Страница товара'

    def should_be_product_page(self):
        self.should_be_product_url()
        self.go_add_product_to_basket()
        self.solve_quiz_and_get_code()

    def go_add_product_to_basket(self):
        """ метод добавления товара в корзину """
        btn_add_to_basket = self.browser.find_element(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET)
        btn_add_to_basket.click()

    def should_be_product_url(self):
        # реализуйте проверку на корректный url адрес
        assert '?promo=newYear' in self.browser.current_url, "Current url does not contain product page"
