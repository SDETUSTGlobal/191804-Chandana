Feature:Test Gmail
  Scenario: open gmail Account
    Given visit gmail website
    Then enter username
    When click next to enter password
    Then enter password
    Then click on login