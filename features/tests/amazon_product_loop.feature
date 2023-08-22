
Feature: verify every product on amazon search results had name and image

  Scenario: verify the product name and image on amazon search result
    Given Open amazon page
    When searching for Tea
    Then Verify search result is "Tea"
    Then Verify the product name and image

