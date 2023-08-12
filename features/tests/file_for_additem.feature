# Created by anithamurali at 8/11/23
Feature: verify the search item on amazon page

  Scenario Outline:Verify that a user can search for product
    Given Open Amazon page
    When searching for <product>
    Then verify search result is <search_result>

    Examples:
    |product          |search_result    |
    |headphones       |"headphones"     |
    |iphone           |"iphone"         |
    |coffee           |"coffee"         |
    |spoon            |"spoon"          |
