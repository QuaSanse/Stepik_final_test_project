import time
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest

product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo="


@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.parametrize('promo_offer',
                         [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='fixing this bug right now')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    url = f"{product_link}offer{promo_offer}"
    page = MainPage(browser, url)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_page()
    # time.sleep(15)


@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.smoke
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    pass
    # Открываем страницу товара
    page = MainPage(browser, product_link)
    page.open()
    # Добавляем товар в корзину
    product_page = ProductPage(browser, browser.current_url)
    product_page.go_add_product_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()


@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.smoke
def test_guest_cant_see_success_message(browser):
    pass
    # Открываем страницу товара
    page = MainPage(browser, product_link)
    page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message()


@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.smoke
def test_message_disappeared_after_adding_product_to_basket(browser):
    pass
    # Открываем страницу товара
    page = MainPage(browser, product_link)
    page.open()
    # Добавляем товар в корзину
    product_page = ProductPage(browser, browser.current_url)
    product_page.go_add_product_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    product_page.the_success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
