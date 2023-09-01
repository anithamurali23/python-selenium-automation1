# Created by anithamurali at 8/1/23
Feature: Verify that amazon cart is empty when clicks on the cart icon

  Scenario:  amazon cart is empty when user clicks on the cart icon
    Given  Open amazon page
    When clicks on the cart icon
    Then verify Your Amazon Cart is empty shown