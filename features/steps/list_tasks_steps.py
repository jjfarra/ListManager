from behave import *
from src.TaskList import TaskList


def before_scenario(context, scenario):
    context = {}


@given("list with  task")
def step_impl(context):
    context.task_list = TaskList()
    context.task_list.add_task("Buy Milk")


@when("the user want to display the task")
def step_impl(context):
    display = context.task_list.display_tasks()
    context.display = display


@then("the list contains {display_text}")
def step_impl(context, display_text):
    assert display_text in context.display
