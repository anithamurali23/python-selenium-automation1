from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


GOTO_CART_ICON = (By.CSS_SELECTOR, 'a[href="/gp/cart/view.html?ref_=nav_cart"]')

@when('clicks on the cart icon')
def cart_icon(context):
    # context.driver.find_element(By.CSS_SELECTOR,'a[href="/gp/cart/view.html?ref_=nav_cart"]').click()
    context.app.header.click_cart_icon()
    sleep(4)


@then('verify {text} shown')
def check_cart(context,text):

    # expected_result = 'Your Amazon Cart is empty'
    # actual_result = context.driver.find_element(By.CSS_SELECTOR,'.a-row.sc-your-amazon-cart-is-empty').text
    # assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual{actual_result}'
    context.app.search_result_page.verifying_empty_cart(text)