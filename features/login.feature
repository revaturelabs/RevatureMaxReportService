Feature: Revature Max Login Page

  Background: A user is on the Revature Max login page and is entering the correct credentials
    Given a user is on the login page
    And a user enters the correct username and password

    Scenario: An associate is on the login page and has entered the correct credentials and would like to login
      When the associate pushes the submit button
      Then the associate is redirected to the associate dashboard

    Scenario: An associate is on the login page and has entered the correct credentials and would like to login
      When the associate clicks the enter key
      Then the associate is redirected to the associate dashboard

    Scenario: A trainer is on the login page and has entered the correct credentials and would like to login
      When the trainer pushes the submit button
      Then the trainer is redirected to the trainer dashboard

    Scenario: A trainer is on the login page and has entered the correct credentials and would like to login
      When the trainer clicks the enter key
      Then the trainer is redirected to the trainer dashboard