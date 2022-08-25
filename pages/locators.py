from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    FORM_LOGIN = (By.CSS_SELECTOR, "form#login_form")
    FORM_REGISTER = (By.CSS_SELECTOR, "form#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSEGE_ADDAD_TO_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    MESSEGE_BASKET_TOTAL = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    # MESSEGE_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages > div.alert-info > div > p:nth-child(1) > strong")
    

