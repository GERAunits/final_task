from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOGIN_URL_KEY = 'login'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
    USER_ICON = (By.CLASS_NAME, "icon-user")


class BasketPageLocators:
    BASKET_ITEMS_CONTAINER = (By.CSS_SELECTOR, '#basket_formset .basket-items')
    BASKET_EMPTY_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p[contains(text(),'Your basket is empty')]")


class LoginPageLocators(object):
    LOGIN_URL_KEY = 'login'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    USER_REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    USER_REGISTRATION_PASSWORD_1 = (By.ID, "id_registration-password1")
    USER_REGISTRATION_PASSWORD_2 = (By.ID, "id_registration-password2")
    USER_REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators(object):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    MESSAGE_CART_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
