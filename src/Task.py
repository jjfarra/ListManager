class Task:

    def __init__(self,title):
        self.title = title
        self.status = "In Progress"

    def mark_finish(self):
        self.status = "Done"

    def mark_blocked(self):
        self.status = "Blocked"
