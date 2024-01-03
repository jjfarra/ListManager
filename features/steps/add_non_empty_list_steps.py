from behave import *
from src.TaskList import TaskList


def before_scenario(context, scenario):
    context = {}


@given("a non-empty list")
def step_impl(context):
    todo_list = TaskList()
    todo_list.add_task("Buy a mouse")
    context.task_list = todo_list


@when("the user add one task {task_name}")
def step_impl(context, task_name):
    context.task_list.add_task(task_name)


@then("the list more than {element} task")
def step_impl(context, element):
    assert int(element) < len(context.task_list.tasks)
