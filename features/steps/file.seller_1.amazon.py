from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

BEST_SELLER_LINK = (By.CSS_SELECTOR,'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
LINK_COUNT = (By.CSS_SELECTOR,"._p13n-zg-nav-tab-all_style_zg-tabs-li-div__1YdPR")

@when('Click on the best sellers')
def click_best_seller(context):
    context.driver.find_element(*BEST_SELLER_LINK).click()

@then( 'Verify there are {no_links} links')
def verify_links(context, no_links):
    no_links = int(no_links)
    number_of_links = context.driver.find_elements(*LINK_COUNT)
    assert len(number_of_links) == no_links, f'expected{no_links} but only got {len(number_of_links)}'



