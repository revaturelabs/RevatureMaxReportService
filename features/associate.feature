Feature: look up a particular grade

  Scenario: An associate is on the login page
    When an associate is on the login page
    And the associate enters the correct username and password1
    And the associate pushes the submit button1
    Then the associate is redirected to the associate dashboard1

  Scenario: An associate would like to view a grade using the search bar
      Given the user enters text into the search bar

  Scenario: An associate would like to view edit profile page
    When the associate clicks on the profile icon
    And the associate clicks on the edit profile button
    Then the associate is redirected to the edit profile page

  Scenario: An associate would like to view change password page
    When the associate clicks on the profile icon
    And the associate clicks on the change password button
    Then the associate is redirected to the change password page
