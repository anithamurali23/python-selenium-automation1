Feature: Verify if logged out user can sign in when clicking on Returns aand Orders

  Scenario: Logged out user can sign in when clicking on Returns and Orders
    Given Open amazon page
    When Click Returns and orders
    Then verify sign in page open
    Then email input field is present

