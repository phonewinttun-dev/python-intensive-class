from db import *

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
        if self.user_id:
            if add_tasks_db(self.user_id, new_task.task_name, new_task.task_status):
                print(f"Task : {new_task.task_name} added successfully!")
                return True
            else:
                print("Failed to add task! Something went wrong!")
                return False

    def remove_task(self, task_name):
        if self.user_id:
            if remove_tasks_db(self.user_id, task_name):
                print(f"{task_name} removed successfully!")
                return True
            
    def update_task(self, task_name):
        if self.user_id:
            if update_tasks_db(self.user_id, task_name):
                print("Task status has been marked as completed!")
                return True
            else:
                print("Update failed! Task not found!")

    def list_tasks(self):
        if self.user_id:
            data = view_tasks_db(self.user_id)
            if data: 
                task_count = 1
                for task in data:
                    task_name = task[0]
                    task_status = task[1]
                    print(f"Task Name: {task_name}, Task Status: {task_status}")
                    task_count += 1
    
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
            self.current_username = check_user["username"]
            print("Login successful!")
            return True
        else: 
            print("Invalid credentials!")