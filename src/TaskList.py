from src.Task import Task


class TaskList:

    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def clean_tasks(self):
        self.tasks.clear()

    def list_tasks(self):
        str_list = []
        for idx, task in enumerate(self.tasks, start=1):
            str_list.append(f"{idx}. {task.title} - {task.status}")

    def mark_task(self, idx):
        temp = self.tasks[idx]
        temp.change_status()
        self.tasks[idx] = temp

    def delete_task(self, idx):
        temp = self.tasks.pop(idx)
        return temp
