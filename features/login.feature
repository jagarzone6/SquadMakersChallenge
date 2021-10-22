@login
Feature: Login into SWAG LABS site
  As a user of SWAG LABS site
  I want to Login into the web app
  So that I can interact with the app

  Background:
    Given I have access to saucedemo app

  @happyPath
  Scenario Outline: Login with valid credentials
    When I log in with user "<username>" and password "<password>"
    Then products page should be displayed
    Examples:
      | username                | password     |
      | standard_user           | secret_sauce |
      | problem_user            | secret_sauce |
      | performance_glitch_user | secret_sauce |

  @negative
  Scenario: Login with locked user
    When I log in with user "locked_out_user" and password "secret_sauce"
    Then error message "Epic sadface: Sorry, this user has been locked out." should be displayed
