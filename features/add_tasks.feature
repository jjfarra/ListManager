Feature: Add a task in a list
  Scenario: Add a task on a non-empty list
    Given a non-empty list
    When  the user add a task "Tesis Context"
    Then the list has 2 task

  Scenario: Add a task in a empty list
    Given an empty list
    When the user add a task "Buy Milk"
    Then the list has 1 task
