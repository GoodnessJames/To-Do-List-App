def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "complete": False})
    print(f"Task '{task} added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to show!\nYou can start by adding a new task:)")
        return
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "[✔]" if task["complete"] else "[ ]"
        print(f"{idx}. {status} {task['task']}")

def complete_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = int(input("Enter the number of the task to mark complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["complete"] = True
            print(f"Task '{tasks[task_num - 1]['task']}' marked as complete!")
        else:
            print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = int(input("\nNote: This process cannot be reversed:(\nEnter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            task = tasks.pop(task_num - 1)
            print(f"Task '{task['task']}' deleted!")
        else:
            print("Invalid task number.")