import time
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.check_for_message_product_is_add()
    page.check_for_correct_cart_price()
    time.sleep(7)
