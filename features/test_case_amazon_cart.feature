Feature: Amazon shopping cart functionality

  Scenario Outline: Search for a product and verify the list response
    Given I navigate to the Amazon Login page
    When I fill in the field username with <credential>
    And I click on Continue button
    And I fill in the field password with <credential>
    And I click on Sign In button
    And I am current in Home page
    And I search for the <product>
    Then I validate if the <products> are found in the result page

    Examples:

      | credential       | product | products                                      |
      | valid credential | kindle  | Kindle Paperwhite 8 Gb - Agora à prova d´água |


  Scenario Outline: Add product to cart and verify product is added to the cart successfully
    Given I navigate to the Amazon Login page
    When I fill in the field username with <credential>
    And I click on Continue button
    And I fill in the field password with <credential>
    And I click on Sign In button
    And I am current in Home page
    And I search for the <product>
    And I click on the <wanted> product in the page
    And I add the <wanted> product to the cart with <quantity> and <options>
    Then I validate if the <wanted> is in the cart and if the quantity in the cart is <quantity> with the selected <options>

    Examples:

      | credential       | product | wanted                                        | quantity | options |
      | valid credential | kindle  | Kindle Paperwhite 8 Gb - Agora à prova d´água | 1        | 32gb    |
      | valid credential | kindle  | Kindle Paperwhite 8 Gb - Agora à prova d´água | 2        | 64gb    |
