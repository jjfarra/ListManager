from src.TaskList import TaskList

if __name__ == '__main__':
    while True:
        task_list = TaskList()

        print(f"{'*'*10}Welcomo to To Do List Manager{'*'*10}")
        print("Available commands:")
        print("1. Add Task")
        print("2. List all Tasks")
        print("3. Mark a Task as complete")
        print("4. Clean the List")
        print("5. Delete a Task")
        print("6. Exit")

        option = int(input("Enter your choice: "))

        if option == 1:
            task_name = input("Enter the title of the task: ")
            task_list.add_task(task_name)
            print("Task successfully Added")
        elif option == 2:
            list_taks = task_list.list_tasks()
            for task in list_taks:
                print(task)
        elif option == 3:
            task_idx = input("Enter the index of the task: ")
            if 0 < int(task_idx) >= len(task_list.tasks):
                task_list.mark_task(int(task_idx))
                print("Task successfully completed")
            else:
                print("Invalid Index")
        elif option == 4:
            task_list.clean_tasks()
            print("Tasks successfully Deleted")
        elif option == 5:
            task_idx = input("Enter the index of the task: ")
            if 0 < int(task_idx) >= len(task_list.tasks):
                del_task = task_list.delete_task(int(task_idx))
                print(f"Task successfully Deleted {del_task.title}")
            else:
                print("Invalid index")
        elif option == 6:
            print("Bye! See you soon!")
        else:
            print("Invalid Option ")
