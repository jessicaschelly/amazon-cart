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
    And I select the product with quantity <quantity> and the option <options>
    Then I add it to the cart and validate if the <wanted> product is in the cart and if the quantity in the cart is <quantity> and option is <options>

    Examples:

      | credential       | product | wanted                                        | quantity | options |
      | valid credential | kindle  | Kindle Paperwhite 8 Gb - Agora à prova d´água | 1        | 32 GB   |
      | valid credential | kindle  | Kindle Paperwhite 8 Gb - Agora à prova d´água | 2        | 8 GB    |


  Scenario Outline: Validate the removal of a product in my cart
    Given I navigate to the Amazon Login page
    When I fill in the field username with <credential>
    And I click on Continue button
    And I fill in the field password with <credential>
    And I click on Sign In button
    And I am current in Home page
    And I search for the <product>
    And I click on the <wanted> product in the page
    And I select the product with quantity <quantity> and the option <options>
    And I add it to the cart and validate if the <wanted> product is in the cart and if the quantity in the cart is <quantity> and option is <options>
    And I remove the product from my cart
    Then I see the <message>

    Examples:

      | credential       | product | wanted                                                     | quantity | options | message    |
      | valid credential | kindle  | Kindle Oasis 32Gb - Agora com temperatura de luz ajustável | 1        | 32 GB   | empty cart |