from ToDoListSystem import ToDoSystem
# from file_handling import load_tasks, save_tasks
from task import Task
# from user_class import User


def operation(to_do_system_obj):
    while True:
        to_do_system_obj.main_menu()

        option = input("Choose which option you want to do: ")

        if option == '1':
            task_name = input("Enter the name of task: ")
            task_status = "" 
            while True:
                task_status_input = input("Enter status of the task (pending or incomplete): ").lower()
                if task_status_input in ["pending", "incomplete"]:
                    task_status = task_status_input
                    break
                else:
                    print("Invalid status. Please enter 'pending' or 'incomplete'.")
            
            new_task = Task(task_name, task_status)
            if to_do_system_obj.add_task(new_task): 
                print(f"Task '{task_name}' successfully added.")
            else:
                print("Failed to add task (ensure you are logged in).")

        elif option == '2':
            removed_task_name = input("Enter the name of task you want to remove: ")
            if to_do_system_obj.remove_task(removed_task_name):
                print(f"Task '{removed_task_name}' removed successfully .")
            else:
                print("Task not found or failed to remove.")
            
        elif option == '3': 
            updated_task_name = input("Enter the name of task you want to mark completed: ")
            if to_do_system_obj.update_task(updated_task_name):
                print(f"Task '{updated_task_name}' status updated successfully.")
            else:
                print("Task not found or failed to update.")
            
        elif option == '4':
            to_do_system_obj.list_tasks() 

        elif option == '5': 
            print("Exiting the task management system....")
            break

        else:
            print("Invalid option. Please choose a number from the menu.")


def main():
    to_do_system = ToDoSystem() 

    logged_in = False 

    while not logged_in:
        to_do_system.login_menu()
        auth_opt = input("Choose which option you want to do: ")

        if auth_opt == '1': 
            logged_in = to_do_system.login_account() 
            operation(to_do_system)
        elif auth_opt == '2': 
            registration_successful = to_do_system.register() 
            if registration_successful:
                print("Registration successful! Please login to your account (option 1).")
        elif auth_opt == '3':
            print("Exiting the system.... Goodbye!")
            return 
        else:
            print("Invalid option! Please choose the valid option.")

    print(f"\nWelcome to your To-Do List, {to_do_system.current_username}!")
    print("You are successfully logged in and can now manage your tasks.")
    
    operation(to_do_system)

# This standard Python idiom ensures main() runs only when the script is executed directly.
if __name__ == "__main__":
    main()
