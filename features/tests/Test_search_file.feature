# Created by anithamurali at 8/1/23
Feature: Verify that amazon cart is empty when clicks on the cart icon

  Scenario:  amazon cart is empty when user clicks on the cart icon
    Given  open amazon page
    When clicks on the cart icon
    Then verify the cart is empty