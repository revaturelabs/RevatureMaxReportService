Feature: A trainer would like to do access a few functionalities in trainer view

  Scenario: A trainer is on the login page and has entered the correct credentials and would like to login
    When a trainer is on the login page1
    And the trainer enters the correct username and password1
    And the trainer pushes the submit button1
    Then the trainer is redirected to the trainer dashboard1

  Scenario: A trainer would like to see an associates performance
    When a trainer presses the particular associate

  Scenario: A trainer would like to view a particular associate using the search box
      Given the trainer enters text into the search bar

  Scenario: A trainer would like to logout
      When the trainer presses the logout button
      Then the trainer is redirected to the login page