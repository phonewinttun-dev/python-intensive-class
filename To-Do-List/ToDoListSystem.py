
class ToDoSystem:
    def main_menu(self):
        print("======================")
        print("1. Create a new task")
        print("2. Remove a task")
        print("3. Update a task")
        print("4. View all the tasks")
        print("5. Exit")
        print("======================")

    def __init__(self, tasks):
        self.tasks = tasks

    def add_task(self, new_task):
        self.tasks.append(new_task)
        return True

    def remove_task(self, task_name):
        for task in self.tasks: 
            if task.task_name == task_name:
                self.tasks.remove(task)
                return True
        return False

    def update_task(self, task_name):
        for task in self.tasks:
            if task.task_name == task_name:
                task.task_status = "Completed"
                return True
        return False

    def list_tasks(self):
        for task in self.tasks:
            print(f"Task Name: {task.task_name}, Status: {task.task_status}")