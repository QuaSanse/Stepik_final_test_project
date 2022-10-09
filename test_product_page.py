from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest

# страница товара с промо
product_link_promo = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo="
# страница товара
product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer',
                         [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='fixing this bug right now')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    url = f"{product_link_promo}offer{promo_offer}"
    page = MainPage(browser, url)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_url()
    product_page.should_be_product_page()


@pytest.mark.smoke
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    page = MainPage(browser, product_link)
    page.open()
    # Добавляем товар в корзину
    product_page = ProductPage(browser, browser.current_url)
    product_page.go_add_product_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()


@pytest.mark.smoke
def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара
    page = MainPage(browser, product_link)
    page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message()


@pytest.mark.smoke
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    page = MainPage(browser, product_link)
    page.open()
    # Добавляем товар в корзину
    product_page = ProductPage(browser, browser.current_url)
    product_page.go_add_product_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    product_page.the_success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    page = ProductPage(browser, product_link)
    page.open()
    # Переходит в корзину по кнопке в шапке
    page.go_to_cart()
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_no_items_in_the_cart()


@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage:
    """ класс проверок для зарегистрированных пользователей """

    def test_user_cant_see_success_message(self, setup, browser):
        """ метод проверки что нет сообщения о добавленных товаров """
        # Открываем страницу товара
        page = MainPage(browser, product_link)
        page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, setup, browser):
        page = MainPage(browser, product_link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_be_product_page()
