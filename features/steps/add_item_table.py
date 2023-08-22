from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

SEARCH_INPUT_PRODUCT = (By.ID,'twotabsearchtextbox')
SEARCH_BTN = (By.ID,'nav-search-submit-button')
PRODUCT_NAME = (By.XPATH,'//span[@class="a-color-state a-text-bold"]')
@when('searching for {items}')
def added_item(context,items):
    # context.driver.find_element(*SEARCH_INPUT_PRODUCT).send_keys(items)
    # context.driver.find_element(*SEARCH_BTN).click()
    context.app.header.search_product(items)


@then('verify search result is {expected_text}')
def verify_item(context,expected_text):
    no_item = context.driver.find_element(*PRODUCT_NAME).text
    assert expected_text == no_item, f'Error, expected {expected_text} did not match actual {no_item} '