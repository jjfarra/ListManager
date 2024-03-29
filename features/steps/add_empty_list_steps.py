from behave import *
from src.TaskList import TaskList


def before_scenario(context, scenario):
    context = {}


@given("an empty list")
def step_impl(context):
    todo_list = TaskList()
    context.task_list = todo_list


@when("the user add a task {task_name}")
def step_impl(context, task_name):
    context.task_list.add_task(task_name)


@then("the list has {element} task")
def step_impl(context, element):
    assert int(element) == len(context.task_list.tasks)
