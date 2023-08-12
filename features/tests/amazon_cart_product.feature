
Feature:user check if the product added in the cart


  Scenario:check the number of product added in the cart
    Given Open amazon page
    When search for pencil pouch
    Then click on a specified product
    Then Add to cart
    Then Verify the added item in the cart
