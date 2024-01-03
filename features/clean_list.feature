Feature: Delete all the tasks

  Scenario: Delete all the tasks in the list
    Given a list with tasks
    When the user delete all the tasks
    Then the list is empty