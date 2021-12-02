Feature: Test smartbear website
  Scenario: testing
    Given go to smartbear website
    Then  enter username and password
    Then click on login
    Then click on checkAll and click on uncheckAll
    When select on item
    Then delete selected item

    Then click on view all products
    When click on orders
    Then enter order purchase details
    Then click on logout


