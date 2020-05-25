from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.USER_REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.USER_REGISTRATION_PASSWORD_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.USER_REGISTRATION_PASSWORD_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.USER_REGISTRATION_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_URL_KEY in self.browser.current_url, "Login not presented in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not presented"
