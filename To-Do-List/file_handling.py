from task import Task

#load
def load_tasks(filename):
    tasks = []
    with open (filename, "r") as file:
        for line in file:
            task_name, task_status = line.strip().split(",")
            loaded_task = Task(task_name, task_status)
            tasks.append(loaded_task)
    return tasks

#save
def save_tasks(tasks, filename):
    with open (filename, "w") as file:
        for task in tasks:
            file.write(f"{task.task_name}, {task.task_status}\n")
    