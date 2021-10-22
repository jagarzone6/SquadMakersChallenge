@complete_shopping_order
Feature: Complete shopping order
  As a user of SWAG LABS site
  I want to complete a shopping order
  So that I can purchase the products I selected

  Background:
    Given I have access to saucedemo app
    And I log in with user "standard_user" and password "secret_sauce"
    And products page is displayed

  @happyPath
  Scenario: Complete order with 1 product
    And I add following products to the shopping cart:
      | PRODUCT NAME          |
      | Sauce Labs Bike Light |
    And I go to the shopping cart
    When I complete chekout process with following details:
      | First Name | Last Name | Zip/Postal Code |
      | Jorge      | Garzon    | 111111          |
    Then the order should be completed successfully
    And I should see "Your order has been dispatched, and will arrive just as fast as the pony can get there!" message

  @happyPath
  Scenario: Complete order with mltiple products
    And I add following products to the shopping cart:
      | PRODUCT NAME             |
      | Sauce Labs Backpack      |
      | Sauce Labs Fleece Jacket |
      | Sauce Labs Onesie        |
    And I go to the shopping cart
    When I complete chekout process with following details:
      | First Name | Last Name | Zip/Postal Code |
      | Jorge      | Garzon    | 111111          |
    Then the order should be completed successfully
    And I should see "Your order has been dispatched, and will arrive just as fast as the pony can get there!" message
