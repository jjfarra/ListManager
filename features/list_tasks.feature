Feature: List all the task
  Scenario: List of string to present all tasks
    Given list with  task
    When  the user want to display the task
    Then  the list contains 1. Buy Milk - In Progress
