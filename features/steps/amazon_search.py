from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('click Returns and Orders')
def search_on_amazon(context):
    context.driver.find_element(By.ID,'nav-orders').click()

@then('verify sign in page open')
def sign_in_page_open(context):

    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH,"// h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual{actual_result}'

@then('email input field is present')
def email_field_present(context):
    expected_result = context.driver.find_element(By.XPATH,"// input[@type = 'email']").is_displayed()
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "#ap_email").is_displayed()
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'