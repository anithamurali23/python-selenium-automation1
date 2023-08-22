from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    RETURNS_ORDERS = (By.ID, 'nav-orders')
    SIGN_IN_PAGE = (By.XPATH, "// h1[@class='a-spacing-small']")
    ER_EMAIL_FIELD = (By.XPATH, "// input[@type = 'email']")
    AR_EMAIL_FIELD = (By.CSS_SELECTOR, "#ap_email")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def returns_orders(self):
        self.click(*self.RETURNS_ORDERS)

    def verify_signin(self,expected_text):
        actual_text = self.find_element(*self. SIGN_IN_PAGE).text
        assert actual_text == expected_text, \
            f'Error, expected {expected_text} did not match actual {actual_text}'
    def email_input(self):
        expected_text = self.display(*self.ER_EMAIL_FIELD)
        actual_text = self.display(*self. AR_EMAIL_FIELD)
        assert actual_text == expected_text, \
        f'Error, expected {expected_text} did not match actual {actual_text}'