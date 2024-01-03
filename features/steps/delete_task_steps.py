from behave import *
from src.TaskList import TaskList


def before_scenario(context, scenario):
    context = {}


@given("a list contains tasks")
def step_impl(context):
    context.task_list = TaskList()
    context.task_list.add_task("Buy a mouse")
    context.task_list.add_task("Call my father")
    context.task_list.add_task("Visit the Museum")


@given("index {idx} enter by the user")
def step_impl(context, idx):
    task_idx = int(idx)
    context.idx = task_idx


@when("the user delete one the tasks")
def step_impl(context):
    del_task = context.task_list.delete_task(context.idx)
    context.del_task = del_task


@then("the title task is {title}")
def step_impl(context, title):
    assert title == context.del_task.title
