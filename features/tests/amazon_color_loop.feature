# Created by anithamurali at 8/16/23
Feature: verify the color selection of a product using loop and check each color of the product are clickable.


#  Scenario: verify a product color by clicking
#    Given Open Amazon product B07BJKRR25 page
#    Then verify the user can click through colors

  Scenario Outline: Select a product from Closing category and hover over New Arrivals
    Given Open Amazon page
    When  searching for <product>
    Then Select one product hoodie
    When Hover over New Arrivals
    Then Verify that the user sees the deals
    Examples:
      | product             |
      | girls pants |