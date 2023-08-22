from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


INPUT_SEARCH = (By.ID,'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID,'nav-search-submit-button')
SP_PRODUCT = (By.CSS_SELECTOR,'.a-section.aok-relative.s-image-square-aspect')
BUTTON_FOR_ADD_TO_CART = (By.CSS_SELECTOR,'#add-to-cart-button')
GO_TO_CART = (By.CSS_SELECTOR, 'a[href="/cart?ref_=sw_gtc"]')
SUB_TOTAL_BTN = (By.CSS_SELECTOR, '#sc-subtotal-label-buybox')
@when('search for pencil pouch')
def search_on_pencil_pouch(context):
    # context.driver.find_element(*INPUT_SEARCH).send_keys('pencil pouch')
    # context.driver.find_element(*SEARCH_BUTTON).click()
    # context.driver.wait.until(EC.element_to_be_clickable(SEARCH_BUTTON)).click()
      context.app.header.search_product('pencil pouch')


@then('click on a specified product')
def click_product(context):
    #context.driver.find_element(*SP_PRODUCT).click()
    context.driver.wait.until(EC.element_to_be_clickable(SP_PRODUCT)).click()

@then('Add to cart')
def cart_add(context):
    context.driver.find_element(*BUTTON_FOR_ADD_TO_CART).click()
    #context.driver.find_element(By.CSS_SELECTOR,'.a-button-input[aria-labelledby="mbc-buybutton-addtocart-1-announce"]').click()
    #context.driver.find_element(By.CSS_SELECTOR,'.a-button-input[aria-labelledby="attachSiNoCoverage-announce"]').click()
    #context.driver.find_element(*GO_TO_CART).click()
    context.driver.wait.until(EC.element_to_be_clickable(GO_TO_CART)).click()

@then('Verify the added item in the cart')
def item_added(context):
    expected_result = 'Subtotal (1 item):'
    actual_result = context.driver.find_element(*SUB_TOTAL_BTN).text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

