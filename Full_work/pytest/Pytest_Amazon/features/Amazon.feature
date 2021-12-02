Feature: Test Amazon
  Scenario: Order item
    Given visit amazon website
    Then  Search for an item
    When  item found
    Then  select item
    Then  order item
