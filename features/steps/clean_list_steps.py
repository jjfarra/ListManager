from behave import *
from src.TaskList import TaskList


def before_scenario(context, scenario):
    context = {}


@given("a list with tasks")
def step_impl(context):
    context.task_list = TaskList()
    context.task_list.add_task("Buy a mouse")
    context.task_list.add_task("Call my father")
    context.task_list.add_task("Visit the Museum")


@when("the user delete all the tasks")
def step_impl(context):
    context.task_list.clean_tasks()


@then("the list is empty")
def step_impl(context):
    assert 0 == len(context.task_list.tasks)
