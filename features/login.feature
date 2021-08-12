Feature: Revature Max Login Page
  Background: A user is on the login page
    Given a user is on the login page

    Scenario: An associate is on the login page and has entered the correct credentials and would like to login
      When the associate enters the correct username and password
      And the associate pushes the submit button
      Then the associate is redirected to the associate dashboard

    Scenario: An associate is on the login page and has entered the correct credentials and would like to login
      When the associate enters the correct username and password
      And the associate clicks the enter key
      Then the associate is redirected to the associate dashboard

    Scenario: A trainer is on the login page and has entered the correct credentials and would like to login
      When the trainer enters the correct username and password
      And the trainer pushes the submit button
      Then the trainer is redirected to the trainer dashboard

    Scenario: A trainer is on the login page and has entered the correct credentials and would like to login
      When the trainer enters the correct username and password
      And the trainer clicks the enter key
      Then the trainer is redirected to the trainer dashboard