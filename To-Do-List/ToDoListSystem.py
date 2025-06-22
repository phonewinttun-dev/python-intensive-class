from db import add_user, check_user_exists

class ToDoSystem:

    def main_menu(self):
        print("======================")
        print("1. Create a new task")
        print("2. Remove a task")
        print("3. Update a task status")
        print("4. View all the tasks")
        print("5. Exit")
        print("======================")



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

    
    def login_menu(self):
        print("You need to login or register first to use our system")
        print("1. Login to your account")
        print("2. Register a new account")
        print("3. Exit")

    def register(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_id = add_user(username, password)
        return user_id

    def login_account(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        check_user = check_user_exists(username, password)
        if check_user:
            self.user_id = check_user["user_id"]
            self.username = check_user["username"]
            print("Login successful!")
            return True
        else: 
            print("Invalid credentials!")