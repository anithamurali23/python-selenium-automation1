# Created by anithamurali at 8/10/23
Feature: Verify if amazon best seller page will open


  Scenario: amazon best seller page will open
    Given open amazon page
    When Click on the best sellers
    Then Verify there are 4 links
