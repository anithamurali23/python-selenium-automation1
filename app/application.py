from pages.main_page import MainPage
from pages.blog import Blog
from pages.not_found_page import NotFoundPage
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.signin_page import SignInPage
from pages.bestseller_page import Best_seller_page
from pages.term_and_condition_page import TermAndConditionPage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)
        self.signin_page = SignInPage(driver)
        self.bestseller_page = Best_seller_page(driver)
        self.blog = Blog(driver)
        self.not_found_page = NotFoundPage(driver)
        self.term_and_condition_page = TermAndConditionPage(driver)
