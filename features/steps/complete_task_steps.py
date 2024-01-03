from behave import *
from src.TaskList import TaskList


def before_scenario(context, scenario):
    context = {}


@given("a list with one task")
def step_impl(context):
    context.task_list = TaskList()
    context.task_list.add_task("Withdraw some money")


@given("users enter index {idx}")
def step_impl(context, idx):
    context.user_index = int(idx)


@when("the user mark as complete")
def step_impl(context):
    context.task_list.mark_complete(context.user_index)


@then("the task's status is {status}")
def step_impl(context, status):
    assert status == context.task_list.tasks[context.user_index - 1].status
