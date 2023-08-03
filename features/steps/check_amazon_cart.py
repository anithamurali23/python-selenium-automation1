from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

@when('search for bread')
def search_on_bread(context):
    context.driver.find_element(By.ID,'twotabsearchtextbox').send_keys('bread')
    context.driver.find_element(By.ID,'nav-search-submit-button').click()
    sleep(2)


@Then('click on a specified product')
def click_product(context):
    context.driver.find_element(By.CSS_SELECTOR,'.a-section.aok-relative.s-image-square-aspect').click()
    sleep(2)

@Then('Add to cart')
def cart_add(context):
    context.driver.find_element(By.CSS_SELECTOR,'#add-to-cart-button').click()
    sleep(2)
    #context.driver.find_element(By.CSS_SELECTOR,'.a-button-input[aria-labelledby="mbc-buybutton-addtocart-1-announce"]').click()
    context.driver.find_element(By.CSS_SELECTOR,'.a-button-input[aria-labelledby="attachSiNoCoverage-announce"]').click()
    context.driver.find_element(By.CSS_SELECTOR, 'a[href="/cart?ref_=sw_gtc"]').click()

    sleep(2)

@Then('Verify the added item in the cart')
def item_added(context):
    expected_result = 'Subtotal (1 item):'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '#sc-subtotal-label-buybox').text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    sleep(2)
