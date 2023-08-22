Feature: Verify if logged out user can sign in when clicking on Returns and Orders

  Scenario: Logged out user can sign in when clicking on Returns and Orders
    Given Open amazon page
    When Click Returns and orders
    Then verify Sign in page open
    Then email input field is present

