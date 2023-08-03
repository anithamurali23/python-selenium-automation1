
Feature:user check if the product added in the cart


  Scenario:check the number of product added in the cart
    Given open amazon page
    When search for bread
    Then click on a specified product
    Then Add to cart
    Then Verify the added item in the cart
