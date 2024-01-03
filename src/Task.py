class Task:

    def __init__(self,title):
        self.title = title
        self.status = "In Progress"

    def change_status(self):
        self.status = "Done"
