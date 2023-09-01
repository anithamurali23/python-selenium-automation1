from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

# BEST_SELLER_LINK = (By.CSS_SELECTOR,'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
# LINK_COUNT = (By.CSS_SELECTOR,'#zg_header a')

TOP_MENU = (By.CSS_SELECTOR, 'div.celwidget.c-f ul a')

@when('Click on the best sellers')
def click_best_seller(context):
    # context.driver.find_element(*BEST_SELLER_LINK).click()
    context.app.header.click_bestseller_btn()


@then( 'Verify there are {no_links} top menu')
def verify_links(context, no_links):
    context.app.bestseller_page.verify_top_menu_count(no_links)


@then('verify all 5 top menu page opens')
def verify_top_menu_page_opens(context):
    expected_text_top_menu = ['Amazon Best Sellers', 'Amazon Hot New Releases',
                              'Amazon Movers & Shakers', 'Amazon Most Wished For',
                              'Amazon Gift Ideas']
    actual_text_top_menu = []

    top_menu_links = context.driver.find_elements(*TOP_MENU)
    for menu_link in top_menu_links[:]:
        menu_link.click()
        shown_top_menu = context.app.bestseller_page.get_text_top_menu()
        actual_text_top_menu.append(shown_top_menu)
        return top_menu_links
    assert actual_text_top_menu == expected_text_top_menu, f'Expected {expected_text_top_menu} did not match actual {actual_text_top_menu}'




