Feature: Change password

  Scenario: A user is on the password change page and enters their correct old password and new password
    When the user pushes the submit button
    Then the user gets a successful message

  Scenario: A user is on the password change page and enters their wrong old password and new password
    When the user pushes the submit button
    Then the user gets an unsuccessful message