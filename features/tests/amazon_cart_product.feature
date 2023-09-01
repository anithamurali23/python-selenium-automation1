
Feature:user check if the product added in the cart


  Scenario:check the number of product added in the cart
    Given Open amazon page
    When search for pencil pouch
    Then click on a specified product
#    When waiting for 4 sec
    Then Add to cart
#    When waiting for 4 sec
    Then Verify the Subtotal (1 item): in the cart









