from src.Task import Task


class TaskList:

    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def clean_tasks(self):
        self.tasks.clear()

    def display_tasks(self):
        str_list = []
        for idx, task in enumerate(self.tasks, start=1):
            str_list.append(f"{idx}. {task.title} - {task.status}")
        return str_list

    def mark_complete(self, idx):
        temp = self.tasks[idx - 1]
        temp.mark_finish()
        self.tasks[idx - 1] = temp

    def blocked(self, idx):
        temp = self.tasks[idx - 1]
        temp.mark_blocked()
        self.tasks[idx - 1] = temp

    def delete_task(self, idx):
        temp = self.tasks.pop(idx - 1)
        return temp


