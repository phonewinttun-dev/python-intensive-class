from ToDoListSystem import ToDoSystem
from file_handling import load_tasks, save_tasks
from task import Task

def main():
    tasks = load_tasks("tasks.txt")
    to_do_system = ToDoSystem(tasks)
    
    while True:
        to_do_system.main_menu()

        option = input("Choose which option you want to do: ")

        if option == '1':
            task_name = input("Enter the name of task: ")
            while True:
                task_status = input("Enter status of the task(pending or incomplete): ")
                if task_status in ["pending", "incomplete"]:
                    break
                else:
                    print("Invalid status. Please enter 'pending' or 'incomplete'.")
            new_task = Task(task_name, task_status)
            to_do_system.add_task(new_task)
            save_tasks(to_do_system.tasks, "tasks.txt")

        elif option == '2':
            removed_task_name = input("Enter the name of task you want to remove: ")
            to_do_system.remove_task(removed_task_name)

        elif option == '3':
            updated_task_name = input("Enter the name of task you want to change status: ")
            to_do_system.update_task(updated_task_name)

        elif option == '4':
            to_do_system.list_tasks()

        elif option == '5':
            print("Exiting the system....")
            break

        else:
            print("Invalid option")

main()