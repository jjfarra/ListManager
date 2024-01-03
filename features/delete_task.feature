Feature: Delete one the tasks

  Scenario: Delete one the tasks in the list
    Given a list contains tasks
    Given index 3 enter by the user
    When the user delete one the tasks
    Then the title task is Visit the Museum