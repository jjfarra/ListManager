Feature: Mark a task as complete

  Scenario: Change the task's status
    Given a list with one task
    Given users enter index 1
    When the user mark as complete
    Then the task's status is Done