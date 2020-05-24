from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_product_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def check_for_message_product_is_add(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name == added_product_name, "Added item isn't equal product: {} != {} with URL: {}" \
            .format(product_name, added_product_name, self.browser.current_url)

    def check_for_correct_cart_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_total_price = self.browser.find_element(*ProductPageLocators.MESSAGE_CART_PRICE).text
        assert product_price == cart_total_price, "Wrong cart price when added item: {} != {}" \
            .format(product_price, cart_total_price)
