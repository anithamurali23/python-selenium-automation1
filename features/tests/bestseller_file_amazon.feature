# Created by anithamurali at 8/10/23
Feature: Verify if amazon best seller page will open


  Scenario: amazon best seller page will open
    Given Open amazon page
    When Click on the best sellers
    Then Verify there are 5 top menu
    Then verify all 5 top menu page opens
