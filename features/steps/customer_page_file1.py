from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

CUSTOMER_SERVICE = (By.CSS_SELECTOR,'a[href="/gp/help/customer/display.html?nodeId=508510&ref_=nav_cs_customerservice"]')
HEADER_CHECK = (By.CSS_SELECTOR,'.fs-heading.bolded[style="color: white;"]')
UI_CONTAINER = (By.CSS_SELECTOR, '.issue-card-container')
UI_LINKS = (By.CSS_SELECTOR,'.issue-card-wrapper')
SEARCH_LIBRARY = (By.XPATH,'//h2[text()="Search our help library"]')
INPUT_SEARCH_CHECK = (By.CSS_SELECTOR,'.a-input-text.a-span12')
ALL_HELP_LIBRARY = (By.XPATH,'//h2[text()="All help topics"]')
HELP_LINK_LIBRARY = (By.CSS_SELECTOR,'.help-topics')



@when('click on customer service button')
def click_customer(context):
    context.driver.find_element(*CUSTOMER_SERVICE).click()


@then('check for header is shown')
def UI_elements(context):
    context.driver.find_element(*HEADER_CHECK)

@then('check for UI box')
def UI_box_con(context):
    context.driver.find_element(*UI_CONTAINER)

@then('verify all {n1} UI element')
def verify_UI(context, n1):
    n1 = int(n1)
    number1_of_links = context.driver.find_elements(*UI_LINKS)
    assert len(number1_of_links) == n1, f'expected{n1} but only got {len(number1_of_links)}'

@then('check for search help library')
def search_library(context):
    context.driver.find_element(*SEARCH_LIBRARY)

@then('check for input field for search library')
def input_library(context):
    context.driver.find_element(*INPUT_SEARCH_CHECK)

@then('check for All help library elements')
def all_help(context):
    context.driver.find_element(*ALL_HELP_LIBRARY)


@then('verify all {n3} links present in All help library')
def verify_help_library(context, n3):
    n3 = int(n3)
    no_link = context.driver.find_elements(*HELP_LINK_LIBRARY)
    assert len(no_link) == n3, f'expected{n3} but got {len(no_link)}'

