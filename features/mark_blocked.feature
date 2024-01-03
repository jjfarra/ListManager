Feature: Mark a task as blocked

  Scenario: Blocked a task
    Given list with task
    Given user enter index 1
    When the user mark as blocked
    Then the task is Blocked