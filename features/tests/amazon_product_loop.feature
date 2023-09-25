
Feature: verify every product on amazon search results had name and image

  Scenario: verify the product name and image on amazon search result
    Given Open amazon page
    When searching for Tea
    Then Verify search result is "Tea"
    Then Verify the product name and image


  Scenario Outline: User can select and search in a department
    Given Open Amazon page
    When Select department by alias <dept_name>
    When Searching for <product>
    Then Verify <search_dept> department is selected
    Examples:
    |dept_name    | product_name    |search_dept|
    |Handmade     |Handmade Jewelry  |Handmade  |
    |Books        | Medical books     |Books    |


