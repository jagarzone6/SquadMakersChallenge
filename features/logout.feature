@logout
Feature: Logout from SWAG LABS site
  As a user of SWAG LABS site
  I want to logout from the web app
  So that I can safely stop using my session

  Background:
    Given I have access to saucedemo app

  @happyPath
  Scenario: Logout from SWAG LABS site
    And I log in with user "standard_user" and password "secret_sauce"
    And products page should be displayed
    When I attempt to logout from the website
    Then I should see login page
