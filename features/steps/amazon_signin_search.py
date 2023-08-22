from behave import given, when, then
from selenium.webdriver.common.by import By

RETURNS_ORDERS = (By.ID,'nav-orders')
SIGN_IN_PAGE = (By.XPATH,"// h1[@class='a-spacing-small']")
ER_EMAIL_FIELD = (By.XPATH,"// input[@type = 'email']")
AR_EMAIL_FIELD = (By.CSS_SELECTOR, "#ap_email")
@given('Open amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()

@when('click Returns and Orders')
def click_reurns(context):
    # context.driver.find_element(*RETURNS_ORDERS).click()
    context.app.header.returns_orders()

@then('verify {text} page open')
def sign_in_page_open(context,text):

    # expected_result = 'Sign in'
    # actual_result = context.driver.find_element(*SIGN_IN_PAGE).text
    # assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual{actual_result}'
     context.app.header.verify_signin(text)
@then('email input field is present')
def email_field_present(context):
    # expected_result = context.driver.find_element(*ER_EMAIL_FIELD).is_displayed()
    # actual_result = context.driver.find_element(*AR_EMAIL_FIELD).is_displayed()
    # assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    context.app.header.email_input()