from behave import *
from src.TaskList import TaskList


def before_scenario(context, scenario):
    context = {}


@given("list with task")
def step_impl(context):
    context.task_list = TaskList()
    context.task_list.add_task("Withdraw some money")


@given("user enter index {idx}")
def step_impl(context, idx):
    context.user_index = int(idx)


@when("the user mark as blocked")
def step_impl(context):
    context.task_list.blocked(context.user_index)


@then("the task is {status}")
def step_impl(context, status):
    print(status)
    print(context.task_list.tasks[context.user_index - 1])
    assert status == context.task_list.tasks[context.user_index - 1].status
