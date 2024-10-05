from datetime import datetime


def add_task(tasks):
    task_description = input("Enter the task description: ")
    category = input("Enter the task category (e.g., Personal, Work, Fun): ")

    while True:
        deadline = input("Enter the task deadline (YYYY-MM-DD HH:MM) ")
        try:
            deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("Invalid date format. Please use this format: YYYY-MM-DD HH:MM")
            # deadline = datetime.now()

    tasks.append({
        "task": task_description, 
        "complete": False, 
        "category": category,
        "deadline": deadline
    })
    print(f"Task '{task_description}' added with deadline '{deadline}'!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to show!\nYou can start by adding a new task:)")
        return
        
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "[✔]" if task["complete"] else "[ ]"

        if isinstance(task["deadline"], datetime):
            deadline_str = task["deadline"].strftime("%Y-%m-%d %H:%M")
        else: 
            deadline_str = task["deadline"] if task.get("deadline") else "No deadline set"
        print(f"{idx}. {status} {task['task']} (Category: {task.get('category', 'None')}), Deadline: {deadline_str}")

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