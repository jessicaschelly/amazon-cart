Feature: Login in Amazon website

  Scenario Outline: Validate Successful Login and Logout on Amazon Website
    Given I navigate to the Amazon Login page
    When I fill in the field username with <credential>
  
    And I fill in the field password with <credential>
    And I click on Sign In button
    And I am current in Home page
    And I click on Logout button

   Examples:

  |credential      |
  |valid credential|

  Scenario Outline: Query an invalid login
    Given I navigate to the Amazon Login page
    When I fill in the field username with <credential>
    And I click on Continue button
    And I fill in the field password with <credential>
    And I click on Sign In button
    Then the Login page should have an error message: <message>

   Examples:

  |credential          |message                             |
  |email not registered|email not found                     |
  |invalid credential  |invalid credential                  |
  |no email            |empty email field                   |
  |no password         |empty password field                |
  |invalid email format|invalid format email